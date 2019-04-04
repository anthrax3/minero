import os
import traceback
import sys
import logging
from textblob import TextBlob as TextBlobModel
import nltk
from miner.services.downloader import Downloader
from miner.services.models import Models
from miner.services.models import Model

logger = logging.getLogger(__name__)

class TextBlob:

    def __init__(self):
        self.models = TextBlobModels()
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
        return {'translation': str(model.translate(to=language))}

    def detect_language(self, document):
        model = TextBlobModel(document)
        return {'language': model.detect_language()}



class TextBlobModels(Models):
   def __init__(self):
       Models.__init__(self);
       self.models_path = os.path.join(self.models_path, 'nltk')

       self.models = dict()
       self.add(Model(
           name = 'nltk',
           description = 'brown, punkt, wordnet, averaged_perceptron_tagger, conll2000, movie_reviews',
           size = '35MB',
           downloader = NltkDownloader(
               'nltk',
               url='https://www.nltk.org/data.html',
               path=self.models_path)
           ))


class NltkDownloader(Downloader):
   def __init__(self, name, *args, **kwargs):
        Downloader.__init__(self, *args, **kwargs)
        self.name = name
        self.models_path = self.path
        self.ensure_models_path()
        nltk.data.path.append(self.models_path);

   def on_download(self):
        import nltk
        nltk.download('brown', download_dir=self.models_path)
        self.current_percentage = 10
        nltk.download('punkt', download_dir=self.models_path)
        self.current_percentage = 20
        nltk.download('wordnet', download_dir=self.models_path)
        self.current_percentage = 40
        nltk.download('averaged_perceptron_tagger', download_dir=self.models_path)
        self.current_percentage = 60
        nltk.download('conll2000', download_dir=self.models_path)
        self.current_percentage = 80
        nltk.download('movie_reviews', download_dir=self.models_path)
        self.current_percentage = 100
        

   def is_downloaded(self):
       downloaded_models = os.listdir(self.models_path)
       if 'corpora' in downloaded_models and 'taggers' in downloaded_models and 'tokenizers' in downloaded_models:
           return True
       return False

   def ensure_models_path(self):
      if not os.path.exists(self.models_path):
         os.makedirs(self.models_path)