import os
import traceback
import sys
import logging
from textblob import TextBlob as TextBlobModel
from cerebro.services.downloader import Downloader

logger = logging.getLogger(__name__)

class TextBlob:

    def __init__(self):
        pass

    def nlp(self, document):
        model = TextBlobModel(document)
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
        return result

    def spelling_correction(self, document):
        model = TextBlobModel(document)
        return {'correct': str(model.correct())}

    def translate(self, document, language):
        model = TextBlobModel(document)
        return {'translation ': str(model.translate(to=language))}

    def detect_language(self, document):
        model = TextBlobModel(document)
        return {'language': model.detect_language()}