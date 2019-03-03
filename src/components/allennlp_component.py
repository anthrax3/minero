import os
import traceback
import sys
import logging
from allennlp.predictors.predictor import Predictor
from services.downloader import Downloader
from services.models import Models
from services.models import Model

logger = logging.getLogger(__name__)

class AllenNlp(object):
   
   def __init__(self):
       self.models = AllenNlpModels()
       pass

   def machine_comprehension(self, document, question):
        try:
           successful, prediction = self.models.try_run('machine_comprehension', 
              passage = document,
              question = question)
           if not successful:
              return prediction
           return {'answer': prediction['best_span_str'],'answer_span': prediction['best_span']}
        except Exception as e:
            logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
            return {"error": str(e)}

   def named_entity_recognition(self, document):
        try:
           successful, prediction = self.models.try_run('named_entity_recognition', 
              sentence = document)
           if not successful:
              return prediction
           return prediction
        except Exception as e:
            logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
            return {"error": str(e)}

   def textual_entailment(self, document, hypothesis):
        try:
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
        except Exception as e:
            logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
            return {"error": str(e)}

   def coreference_resolution(self, document):
        try:
          successful, prediction = self.models.try_run('coreference_resolution', 
             document = document)
          if not successful:
              return prediction
          return prediction
        except Exception as e:
            logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
            return {"error": str(e)}

   def semantic_role_labeling(self, document):
        try:
          successful, prediction = self.models.try_run('semantic_role_labeling', 
             sentence = document)
          if not successful:
              return prediction
          return prediction           
        except Exception as e:
            logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
            return {"error": str(e)}

   def constituency_parsing(self, document):
        try:
          successful, prediction = self.models.try_run('constituency_parsing', 
             sentence = document)
          if not successful:
              return prediction
          return prediction           
        except Exception as e:
            logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
            return {"error": str(e)}
   
   def dependency_parsing(self, document):
        try:
          successful, prediction = self.models.try_run('dependency_parsing', 
             sentence = document)
          if not successful:
              return prediction
          return prediction
        except Exception as e:
            logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
            return {"error": str(e)}

   def open_information_extraction(self, document):
        try:
          successful, prediction = self.models.try_run('open_information_extraction', 
             sentence = document)
          if not successful:
              return prediction
          return prediction           
        except Exception as e:
            logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
            return {"error": str(e)}
  
   def event2mind(self, document):
        try:
          successful, prediction = self.models.try_run('event2mind', 
             source = document)
          if not successful:
              return prediction
          return prediction
        except Exception as e:
            logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
            return {"error": str(e)}

  

class AllenNlpModels(Models):
   def __init__(self):
       Models.__init__(self);
       self.models_path = os.path.join(self.models_path, 'allennlp')
       self.add(Model(
           name = 'machine_comprehension',
           displayName = 'bidaf-model-2017.09.15-charpad.tar.gz',
           description = 'Reimplementation of BiDAF (Seo et al, 2017)',
           size = '44MB',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz',
               path=os.path.join(self.models_path,'bidaf-model-2017.09.15-charpad.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'named_entity_recognition',
           displayName = 'ner-model-2018.12.18.tar.gz',
           description = 'Reimplementation of the state-of-the-art NER model described in Deep contextualized word representations, and uses a biLSTM with CRF layer and ELMo embeddings',
           size = '678MB',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/ner-model-2018.12.18.tar.gz',
               path=os.path.join(self.models_path,'ner-model-2018.12.18.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'textual_entailment',
           displayName = 'decomposable-attention-elmo-2018.02.19.tar.gz',
           description = 'Reimplementation of the decomposable attention model (Parikh et al, 2017)',
           size = '665MB',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/decomposable-attention-elmo-2018.02.19.tar.gz',
               path=os.path.join(self.models_path,'decomposable-attention-elmo-2018.02.19.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'coreference_resolution',
           displayName = 'coref-model-2018.02.05.tar.gz',
           description = 'Implementation is based on End-to-End Coreference Resolution (Lee et al, 2017)',
           size = '57MB',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/coref-model-2018.02.05.tar.gz',
               path=os.path.join(self.models_path,'coref-model-2018.02.05.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'semantic_role_labeling',
           displayName = 'srl-model-2018.05.25.tar.gz',
           description = 'Reimplementation of a deep BiLSTM model (He et al, 2017)',
           size = '697MB',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz',
               path=os.path.join(self.models_path,'srl-model-2018.05.25.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'constituency_parsing',
           displayName = 'elmo-constituency-parser-2018.03.14.tar.gz',
           description = 'Independent scoring of labels and spans from Minimal Span Based Constituency Parser (Stern et al, 2017)',
           size = '677MB',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/elmo-constituency-parser-2018.03.14.tar.gz',
               path=os.path.join(self.models_path,'elmo-constituency-parser-2018.03.14.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'dependency_parsing',
           displayName = 'biaffine-dependency-parser-ptb-2018.08.23.tar.gz',
           description = 'Implementation of a neural model for dependency parsing using biaffine classifiers on top of a bidirectional LSTM based on Deep Biaffine Attention for Neural Dependency Parsing (Dozat, 2017)',
           size = '70MB',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/biaffine-dependency-parser-ptb-2018.08.23.tar.gz',
               path=os.path.join(self.models_path,'biaffine-dependency-parser-ptb-2018.08.23.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'open_information_extraction',
           displayName = 'openie-model.2018-08-20.tar.gz',
           description = 'Reimplementation of a deep BiLSTM sequence prediction model (Stanovsky et al., 2018)',
           size = '63MB',
           downloader = Downloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/openie-model.2018-08-20.tar.gz',
               path=os.path.join(self.models_path,'openie-model.2018-08-20.tar.gz'),
               overwrite=True)
           ))
       self.add(Model(
           name = 'event2mind',
           displayName = 'event2mind-2018.09.17.tar.gz',
           description = 'Reimplementation of the original Event2Mind neural inference model (Rashkin et al, 2018)',
           size = '52MB',
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
          
