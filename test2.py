from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def language_analysis(text):
        client = language.LanguageServiceClient()   ###  Hashed code is Old code as per video 
        #document = client.document_from_text(text)
        document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

        #sent_analysis = client.analyze_sentiment()
        sent_analysis = client.analyze_sentiment(document=document).document_sentiment
        print(dir(sent_analysis)) # checking the parameters avaialble
        #sentiment = sent_analysis.sentiment
        #ent_analysis = document.analyze_entities()
        entities = client.analyze_entities(document).entities
        #entities = ent_analysis.entities
        return sent_analysis, entities

#example = u'is it not obvious that python is the best programming language'

### content taken from Python wiki page
example = '''Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python ha


s a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and lar
ge scales.[26]
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and
 procedural, and has a large and comprehensive standard library.[27]
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[28] and has a community-based dev
elopment model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.'''


sentiment, entities = language_analysis(example)
print('Text: {}'.format(example))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
#print(sentiment.score, sentiment.magnit)

entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION', 'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

for e in entities:
        print(('name', e.name), ('type', entity_type[e.type]), ('metadata', e.metadata), ('salience', e.salience), ('wiki-page', e.metadata.get('wikipedia_url', '-')))


##flow = flow_from_clientsecrets('OAUTHsecret2.json',
##                               scope='https://www.googleapis.com/auth/calendar',
##                               redirect_uri='http://example.com/auth_return')
##
##auth_uri = flow.step1_get_authorize_url()
##
##from oauth2client import tools
##>>> import argparse
##>>> parser = argparse.ArgumentParser(parents=[tools.argparser])
##>>> flags = parser.parse_args()
