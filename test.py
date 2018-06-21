#import argparse
#import sentiment_mod as s
from hercules import Hercules
#from google.cloud import language

def language_analysis(text):
    client = language.LanguageServiceClient()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    dir(sent_analysis)
    sentiment = sent_analysis.sentiment

    ent_analysis = document.analyze_entities()
    dir(ent_analysis)
    entities = ent_analysis.entities

    return sentiment, entities

#print(language.Client())

bot = Hercules(["bitcoin","startups","btc","cryptocurrencies","wallet"],100);

#bot.getComments()
#bot.find("bitcoin")

bot.realthing("bitcoin startup",["startup","bitcoin","ledger","cryptocurrencies"])

#I should search for the sentence and then look for the thing.
#
#
#bot.points("bitcoin",["startup","bitcoin","ledger","cryptocurrencies"])
#document = types.Document(
#        content=content,
#        type=enums.Document.Type.PLAIN_TEXT)
#annotations = client.analyze_sentiment(document=document)

    # Print the results
#    print_result(annotations)
#

#bot.something should actually call bot.points which should be called by something else.

# but what exactly is going on is something that I should really think about.


for x in range(len(bot.replyCommentslist)):
    print (bot.BMP(bot.replyCommentslist[x].body))
    #print(s.sentiment(bot.replyCommentslist[x].body))
    #sentiment, entities = language_analysis(bot.replyCommentslist[x].body)
    #print(sentiment.score, sentiment.magnitude)
    #for e in entities:
    #    print(e.name, e.entity_type, e.metadata, e.salience)

#bot.replyCommentslist[0].body Not sure if it should be a separatefunction.
# as the reply depends upon the comment.

#print(len(bot.replyCommentslist))
