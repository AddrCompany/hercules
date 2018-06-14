# import library files here


import praw
import re

def BMP(s): #probably useless function now but maybe needed to print
        return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

class Hercules:

    redditors = []
    replyCommentslist=[]
    numOfThreads=0
    subreddit_name = ""
    commentThread=[]
    userpoint = {}
    r = praw.Reddit(user_agent='Comment Extraction (by u/showbobsandvagene69)',
                     client_id='FoLEE6kIDMG2XQ', client_secret="UfObG0klXZW4EcOWB-bMKO2AaMk",
                     username='showbobsandvagene69', password='casewestern')
    
    def __init__(self,subreddit_name,numOfThreads):
        self.numOfThreads = numOfThreads
        self.subreddit_name = subreddit_name

    def getComments(self):
        subreddit = self.r.subreddit(self.subreddit_name)
        for submission in subreddit.hot(limit=self.numOfThreads):
            submission.comments.replace_more(limit=0)
            submission.comment_sort = 'hot'
            submission.comment_limit = 5 # does not seem to be doing anything.
            print ("Caching comments from thread id:", submission)
            raza = submission.comments.list()
            self.commentThread.append([raza, submission.id])
            #comment_attributes = []
            #for comment in raza:
            #    comment_attributes.append([self.BMP(comment.body),comment.score,comment.id,submission.id])
            #self.commentsList.append(comment_attributes[:])

    def find(self, keyword):
        wordFound = re.compile(r'\b({0})\b'.format(keyword), flags=re.IGNORECASE).search
        for index in range(len(self.commentThread)):
            for comment_attributes in self.commentThread[index][0]:
                if wordFound(comment_attributes.body) is not None:
                    print("\n*********\nWord found in this comment:",comment_attributes.id, "with thread id",comment_attributes.id )
                    self.replyCommentslist.append(comment_attributes)
                    self.redditors.append(comment_attributes.author)

#this function will get an input of a user and find all the posts mentioning a keyword and increment the value by 1 if it exists there or not.
    def userpoints(self,user,keywords):
# a check to see if a user already exists or not. Maybe not necessary as points already makes sure of that.
        sub_count = 0
        dirty_count = 0
        with open("userpoints.txt","r") as f:
            users_already_posted = f.read().split()
        if user.name in users_already_posted:
            return
        else:
            self.userpoint[user] = 0
        # storing 100 comments of the user in tempcomment for a particular user.
        tempcomment = []

        for comment in self.r.redditor(user.name).comments.new(limit=100):
            tempcomment.append(comment)
# finding all keywords in the tempcomments datastructure and finding percentage of dirty_words by posts.
        for x in keywords:
            wordFound = re.compile(r'\b({0})\b'.format(x), flags=re.IGNORECASE).search
            for index in range(len(tempcomment)):
                if wordFound(tempcomment[index].body) is not None:
                    print("Comment is ", BMP(tempcomment[index].body), " user is ", user, "and points are ", self.userpoint[user])
                    # self.userpoint[user] += 1
                    dirty_count += 1
                sub_count += 1
            try:
                trashy_score = dirty_count/sub_count
            except: trashy_score = 0.0
            self.userpoint[user] = trashy_score
            print(" \n ", user, " percentage points = ", self.userpoint[user])
        with open("userpoints.txt","a") as f:
            f.write(user.name + ' ' + ' ' + str(round(trashy_score,4)*100) + ' ' + str(sub_count) + '\n')

#this function will call userpoint for all users.
    def points(self, keywords):
        try:
            for x in set(self.redditors):
                self.userpoints(x, keywords)
        except Exception as e:
            print(str(e))

    def reply(self, commentid, replyList):
        commentid.reply(replyList)   
