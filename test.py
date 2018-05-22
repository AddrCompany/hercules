from hercules import Hercules

bot = Hercules("pakistan",30);

bot.getComments()
bot.find("Nawaz")
#bot.replyCommentslist[0].body Not sure if it should be a separatefunction.
# as the reply depends upon the comment.
