import os
from allennlp.predictors.predictor import Predictor
from services.downloader import Downloader
from services.models import Models
from services.models import Model

class AllenNlp(object):
   
   def __init__(self):
       self.models = AllenNlpModels()
       pass

   def machine_comprehension(self, document, question):
       successful, prediction = self.models.try_run('machine_comprehension', 
          passage = document,
          question = question)
       if not successful:
          return prediction
       return {'answer': prediction['best_span_str'],'answer_span': prediction['best_span']}

   def named_entity_recognition(self, document):
       successful, prediction = self.models.try_run('named_entity_recognition', 
          sentence = document)
       if not successful:
          return prediction
       return prediction

   def textual_entailment(self, document, hypothesis):
      successful, prediction = self.models.try_run('textual_entailment', 
         premise = document,
         hypothesis = hypothesis)
      if not successful:
          return prediction
      return {
          'entailment': prediction['label_probs'][0],
          'contradiction': prediction['label_probs'][1],
          'neutral': prediction['label_probs'][2]
          }

   def coreference_resolution(self, document):
      successful, prediction = self.models.try_run('coreference_resolution', 
         document = document)
      if not successful:
          return prediction
      return prediction

   def semantic_role_labeling(self, document):
      successful, prediction = self.models.try_run('semantic_role_labeling', 
         sentence = document)
      if not successful:
          return prediction
      return prediction

   def constituency_parsing(self, document):
      successful, prediction = self.models.try_run('constituency_parsing', 
         sentence = document)
      if not successful:
          return prediction
      return prediction
   
   def dependency_parsing(self, document):
      successful, prediction = self.models.try_run('dependency_parsing', 
         sentence = document)
      if not successful:
          return prediction
      return prediction

   def open_information_extraction(self, document):
      successful, prediction = self.models.try_run('open_information_extraction', 
         sentence = document)
      if not successful:
          return prediction
      return prediction
  
   def event2mind(self, document):
      successful, prediction = self.models.try_run('event2mind', 
         source = document)
      if not successful:
          return prediction
      return prediction
  

class AllenNlpModels(Models):
   def __init__(self):
       Models.__init__(self);
       self.models_path = os.path.join(self.models_path, 'allennlp')
       self.add(Model(
           name = 'machine_comprehension',
           description = '',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz',
               path=os.path.join(self.models_path,'bidaf-model-2017.09.15-charpad.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'named_entity_recognition',
           description = '',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/ner-model-2018.12.18.tar.gz',
               path=os.path.join(self.models_path,'ner-model-2018.12.18.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'textual_entailment',
           description = '',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/decomposable-attention-elmo-2018.02.19.tar.gz',
               path=os.path.join(self.models_path,'decomposable-attention-elmo-2018.02.19.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'coreference_resolution',
           description = '',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/coref-model-2018.02.05.tar.gz',
               path=os.path.join(self.models_path,'coref-model-2018.02.05.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'semantic_role_labeling',
           description = '',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz',
               path=os.path.join(self.models_path,'srl-model-2018.05.25.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'constituency_parsing',
           description = '',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/elmo-constituency-parser-2018.03.14.tar.gz',
               path=os.path.join(self.models_path,'elmo-constituency-parser-2018.03.14.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'dependency_parsing',
           description = '',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/biaffine-dependency-parser-ptb-2018.08.23.tar.gz',
               path=os.path.join(self.models_path,'biaffine-dependency-parser-ptb-2018.08.23.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'open_information_extraction',
           description = '',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/openie-model.2018-08-20.tar.gz',
               path=os.path.join(self.models_path,'openie-model.2018-08-20.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'event2mind',
           description = '',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/event2mind-2018.09.17.tar.gz',
               path=os.path.join(self.models_path,'event2mind-2018.09.17.tar.gz'),
               overwrite=True)
           ))    

   def load(self, name):
       if name == 'machine_comprehension' and not self.is_loaded(name):
          self.models[name].model = Predictor.from_path(os.path.join(self.models_path, "bidaf-model-2017.09.15-charpad.tar.gz"))
       if name == 'named_entity_recognition' and not self.is_loaded(name):
          self.models[name].model = Predictor.from_path(os.path.join(self.models_path, "ner-model-2018.12.18.tar.gz"))
       if name == 'textual_entailment' and not self.is_loaded(name):
          self.models[name].model = Predictor.from_path(os.path.join(self.models_path, "decomposable-attention-elmo-2018.02.19.tar.gz"))
       if name == 'coreference_resolution' and not self.is_loaded(name):
          self.models[name].model = Predictor.from_path(os.path.join(self.models_path, "coref-model-2018.02.05.tar.gz"))
       if name == 'semantic_role_labeling' and not self.is_loaded(name):
          self.models[name].model = Predictor.from_path(os.path.join(self.models_path, "srl-model-2018.05.25.tar.gz"))
       if name == 'constituency_parsing' and not self.is_loaded(name):
          self.models[name].model = Predictor.from_path(os.path.join(self.models_path, "elmo-constituency-parser-2018.03.14.tar.gz"))
       if name == 'dependency_parsing' and not self.is_loaded(name):
          self.models[name].model = Predictor.from_path(os.path.join(self.models_path, "biaffine-dependency-parser-ptb-2018.08.23.tar.gz"))
       if name == 'open_information_extraction' and not self.is_loaded(name):
          self.models[name].model = Predictor.from_path(os.path.join(self.models_path, "openie-model.2018-08-20.tar.gz"))
       if name == 'event2mind' and not self.is_loaded(name):
          self.models[name].model = Predictor.from_path(os.path.join(self.models_path, "event2mind-2018.09.17.tar.gz"))
          
