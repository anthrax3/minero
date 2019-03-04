from textblob import TextBlob
from textblob.download_corpora import download_all
import json

#import nltk
#nltk.data.path = ["C:\\Projects\\nlp\\src\\cerebro\\models"]

#x = download_all()
#print(x)

document = "Human machine interface for lab abc computer applications.A survey of user opinion of computer system response time. The EPS user interface management system"

model = TextBlob(document)
result = {
    'tokens': [
        {
            'text': text, 
            'tag':model.tags[index][1],
            'singular': model.words[index].singularize(),
            'plurar': model.words[index].pluralize(),
            'lemma': model.words[index].lemmatize(),
        }for index, text in enumerate(model.words)],
    'noun_phrases': model.noun_phrases,
    'sentences': [
        {
            'text':x.raw,
            'start':x.start,
            'end':x.end,
            'sentiment': {'polarity':x.sentiment.polarity, 'subjectivity':x.sentiment.subjectivity}
         } for x in model.sentences],
    'sentiment': {'polarity':model.sentiment.polarity, 'subjectivity':model.sentiment.subjectivity},
}
#sentiment.polarity
#sentiment.subjectivity
print(json.dumps(result))


#Spelling correctionSpelling correction
b = TextBlob("I havv goood speling!")
print(b.correct())

#Translation
en_blob = TextBlob(u'Simple is better than complex.')
print(en_blob.translate(to='es'))

#Language Detection
b = TextBlob(u"بسيط هو أفضل من مجمع")
print(b.detect_language())