import os
import tarfile
import shutil
import spacy
import traceback
import sys
import datetime
import logging
from spacy.util import set_data_path
from miner.services.downloader import Downloader
from miner.services.models import Models
from miner.services.models import Model

logger = logging.getLogger(__name__)

class Spacy:
   def __init__(self):
       self.models = SpacyModels()
       pass

   def nlp(self, model, document):
           is_valid, error = self.models.validate(model)
           if not is_valid:
               return {'error': error}
           self.models.load(model)
           doc_spacy = self.models.get(model).model(document)
           doc_dict = {"entities": [], "tokens": [], "noun_chunks": [], "sentences": []}
           for token in doc_spacy:
               doc_dict["tokens"].append(
                   {
                      "text": token.text,
                      "lemma": token.lemma_,
                      "pos": token.pos_,
                      "tag": token.tag_,
                      "dep_": token.dep_,
                      "shape_,": token.shape_,
                      "is_alpha": token.is_alpha,
                      "is_stop": token.is_stop,
                      "head.tex": token.head.text,
                      "head.pos,": token.head.pos_,
                      "has_vector": token.has_vector, 
                      #"vector_norm": token.vector_norm, 
                      "is_oov": token.is_oov
                      #"children": [child for child in token.children]
                   })

           for chunk in doc_spacy.noun_chunks:
              doc_dict["noun_chunks"].append(
                  {
                      "text": chunk.text, 
                      "root.text": chunk.root.text,
                      "root.dep_": chunk.root.dep_,
                      "label_": chunk.label_,
                      "root.head.text": chunk.root.head.text
                  })

           for sentence in doc_spacy.sents:
              doc_dict["sentences"].append(
                  {
                      "text": sentence.text
                  })

           for entity in doc_spacy.ents:
              doc_dict["entities"].append(
                  {
                      "text": entity.text, 
                      "label": entity.label_,
                      "start": entity.start_char, 
                      "end": entity.end_char
                  })
           
           return doc_dict

   def similarity(self, model, document, similarTo):
           is_valid, error = self.models.validate(model)
           if not is_valid:
               return {'error': error}
           self.models.load(model)
           document_spacy = self.models.get(model).model(document)
           similarTo_spacy = self.models.get(model).model(similarTo)
           prediction = document_spacy.similarity(similarTo_spacy)
           return {'similarity': prediction};

class SpacyModels(Models):
   def __init__(self):
       Models.__init__(self);
       self.models_path = os.path.join(self.models_path, 'spacy')
       set_data_path(self.models_path)
       self.models = dict()
       self.add(Model(
           name = 'en_core_web_sm-2.0.0',
           description = 'English	Vocabulary, syntax, entities',
           size = '35MB',
           downloader = SpacyDownloader(
               'en_core_web_sm-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'en_core_web_sm-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'en_core_web_md-2.0.0',
           description = 'English	Vocabulary, syntax, entities, vectors',
           size = '115MB',
           downloader = SpacyDownloader(
               'en_core_web_md-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.0.0/en_core_web_md-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'en_core_web_md-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'en_core_web_lg-2.0.0',
           description = 'English	Vocabulary, syntax, entities, vectors',
           size = '812MB',
           downloader = SpacyDownloader(
               'en_core_web_lg-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.0.0/en_core_web_lg-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'en_core_web_lg-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'en_vectors_web_lg-2.0.0',
           description = 'English	Word vectors',
           size = '631MB',
           downloader = SpacyDownloader(
               'en_vectors_web_lg-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/en_vectors_web_lg-2.0.0/en_vectors_web_lg-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'en_vectors_web_lg-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'de_core_news_sm-2.0.0',
           description = 'German	Vocabulary, syntax, entities',
           size = '36MB',
           downloader = SpacyDownloader(
               'de_core_news_sm-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/de_core_news_sm-2.0.0/de_core_news_sm-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'de_core_news_sm-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'es_core_news_sm-2.0.0',
           description = 'Spanish	Vocabulary, syntax, entities',
           size = '35MB',
           downloader = SpacyDownloader(
               'es_core_news_sm-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/es_core_news_sm-2.0.0/es_core_news_sm-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'es_core_news_sm-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'es_core_news_md-2.0.0',
           description = 'Spanish	Vocabulary, syntax, entities, vectors',
           size = '93MB',
           downloader = SpacyDownloader(
               'es_core_news_md-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/es_core_news_md-2.0.0/es_core_news_md-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'es_core_news_md-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'pt_core_news_sm-2.0.0',
           description = 'Portuguese	Vocabulary, syntax, entities',
           size = '36MB',
           downloader = SpacyDownloader(
               'pt_core_news_sm-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/pt_core_news_sm-2.0.0/pt_core_news_sm-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'pt_core_news_sm-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'fr_core_news_sm-2.0.0',
           description = 'French	Vocabulary, syntax, entities',
           size = '37MB',
           downloader = SpacyDownloader('fr_core_news_sm-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/fr_core_news_sm-2.0.0/fr_core_news_sm-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'fr_core_news_sm-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'fr_core_news_md-2.0.0',
           description = 'French	Vocabulary, syntax, entities, vectors',
           size = '106MB',
           downloader = SpacyDownloader(
               'fr_core_news_md-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/fr_core_news_md-2.0.0/fr_core_news_md-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'fr_core_news_md-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'it_core_news_sm-2.0.0',
           description = 'Italian	Vocabulary, syntax, entities',
           size = '34MB',
           downloader = SpacyDownloader(
               'it_core_news_sm-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/it_core_news_sm-2.0.0/it_core_news_sm-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'it_core_news_sm-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'nl_core_news_sm-2.0.0',
           description = 'Dutch	Vocabulary, syntax, entities',
           size = '34MB',
           downloader = SpacyDownloader(
               'nl_core_news_sm-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/nl_core_news_sm-2.0.0/nl_core_news_sm-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'nl_core_news_sm-2.0.0.tar.gz'))
           ))
       self.add(Model(
           name = 'xx_ent_wiki_sm-2.0.0',
           description = 'Multi-language	Named entities',
           size = '31MB',
           downloader = SpacyDownloader(
               'xx_ent_wiki_sm-2.0.0',
               url='https://github.com/explosion/spacy-models/releases/download/xx_ent_wiki_sm-2.0.0/xx_ent_wiki_sm-2.0.0.tar.gz',
               path=os.path.join(self.models_path,'xx_ent_wiki_sm-2.0.0.tar.gz'))
           ))

   def load(self, name):
       if self.exists(name) and not self.is_loaded(name):
          model = self.get(name)
          self.models[name].model = spacy.util.load_model_from_path(model.downloader.load_model_path)


class SpacyDownloader(Downloader):
   def __init__(self, name, *args, **kwargs):
        Downloader.__init__(self, *args, **kwargs)
        self.name = name
        self.models_path, self.file_name = os.path.split(self.path)
        self.name_without_version = self.name.split('-')[0]
        self.extracted_model_path = os.path.join(self.models_path, self.name)
        self.load_model_path = os.path.join(self.extracted_model_path, self.name_without_version, self.name)

   def on_downloaded(self):
        self.status = 'ExtractingArchive'
        try:
            shutil.rmtree(self.extracted_model_path, ignore_errors=True)
            if self.path.endswith('tar.gz'):
               with tarfile.open(self.path, 'r:gz') as tar:
                  def is_within_directory(directory, target):
                      
                      abs_directory = os.path.abspath(directory)
                      abs_target = os.path.abspath(target)
                  
                      prefix = os.path.commonprefix([abs_directory, abs_target])
                      
                      return prefix == abs_directory
                  
                  def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                  
                      for member in tar.getmembers():
                          member_path = os.path.join(path, member.name)
                          if not is_within_directory(path, member_path):
                              raise Exception("Attempted Path Traversal in Tar File")
                  
                      tar.extractall(path, members, numeric_owner=numeric_owner) 
                      
                  
                  safe_extract(tar, self.models_path)
        except Exception as e:
            self.status = 'Error'
            self.error = 'Error durring extracting archive: ' + str(e)
            return
        
        self.status = 'ExtractedArchive'
        pass

   def is_downloaded(self):
       self.ensure_path()
       downloaded_models = os.listdir(self.models_path)
       if self.name in downloaded_models:
           return True
       return False