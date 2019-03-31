import os
import traceback
import sys
import logging
import shutil
from allennlp.predictors.predictor import Predictor
from nlp.services.downloader import Downloader
from nlp.services.models import Models
from nlp.services.models import Model
from nlp.components import Spacy

logger = logging.getLogger(__name__)

class AllenNlp(object):
   
   def __init__(self):
       self.models = AllenNlpModels()
       pass

   def machine_comprehension(self, document, question):
           successful, prediction = self.predict('machine_comprehension', 
              passage = document,
              question = question)
           if not successful:
              return prediction
           return {'answer': prediction['best_span_str'],'answer_span': prediction['best_span']}

   def named_entity_recognition(self, document):
           successful, prediction = self.predict('named_entity_recognition', 
              sentence = document)
           if not successful:
              return prediction
           result = {'tokens': []}
           for index, word in enumerate(prediction['words']):
               result['tokens'].append({
                   'text':word,
                   'tag':prediction['tags'][index]
                   });
           return result

   def textual_entailment(self, document, hypothesis):
          successful, prediction = self.predict('textual_entailment', 
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
          successful, prediction = self.predict('coreference_resolution', 
             document = document)
          return prediction

   def semantic_role_labeling(self, document):
          successful, prediction = self.predict('semantic_role_labeling', 
             sentence = document)
          return prediction           

   def constituency_parsing(self, document):
          successful, prediction = self.predict('constituency_parsing', 
             sentence = document)
          if not successful:
             return False, {'error': result}
          result = {'tokens':[], 'spans':prediction['spans'], 'trees':prediction['trees'], 'hierplane_tree':prediction['hierplane_tree']}
          for index, token in enumerate(prediction['tokens']):
             result['tokens'].append({
                'text':token,
                'pos':prediction['pos_tags'][index]
                })
          return result
              
   
   def dependency_parsing(self, document):
          successful, prediction = self.predict('dependency_parsing', 
             sentence = document)
          if not successful:
             return False, {'error': result}
          result = {'tokens':[], 'hierplane_tree':prediction['hierplane_tree']}
          for index, token in enumerate(prediction['words']):
             result['tokens'].append({
                'text':token,
                'pos':prediction['pos'][index],
                'dependency':prediction['predicted_dependencies'][index],
                'head':prediction['predicted_heads'][index],
                })
          return result

   def open_information_extraction(self, document):
          successful, prediction = self.predict('open_information_extraction', 
             sentence = document)
          if not successful:
             return False, {'error': result}
          result = {'verbs':[], 'tokens':prediction['words']}
          for index, verb in enumerate(prediction['verbs']):
              verb_tokens = []
              for index, token in enumerate(prediction['words']):
                  verb_tokens.append({
                      'token':token,
                      'tag':verb['tags'][index]
                      })
              result['verbs'].append({
                  'verb':verb['verb'],
                  'description':verb['description'],
                  'tokens':verb_tokens,
                  })
          return result
  
   def event2mind(self, document):
          successful, prediction = self.predict('event2mind', 
             source = document)
          return prediction

   def predict(self, model_name, *args, **kwargs):
       is_valid, result = self.models.validate(model_name)
       if not is_valid:
           return False, {'error': result}
       self.models.load(model_name)
       model = self.models.get(model_name).model
       prediction =  model.predict(*args, **kwargs)
       return True, prediction

  

class AllenNlpModels(Models):
   def __init__(self):
       Models.__init__(self);
       self.models_path = os.path.join(self.models_path, 'allennlp')
       self.add(Model(
           name = 'machine_comprehension',
           displayName = 'bidaf-model-2017.09.15-charpad.tar.gz',
           description = 'Reimplementation of BiDAF (Seo et al, 2017)',
           size = '44MB',
           downloader = AllennlpDownloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz',
               path=os.path.join(self.models_path,'bidaf-model-2017.09.15-charpad.tar.gz'))
           ))
       self.add(Model(
           name = 'named_entity_recognition',
           displayName = 'ner-model-2018.12.18.tar.gz',
           description = 'Reimplementation of the state-of-the-art NER model described in Deep contextualized word representations, and uses a biLSTM with CRF layer and ELMo embeddings',
           size = '678MB',
           downloader = AllennlpDownloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/ner-model-2018.12.18.tar.gz',
               path=os.path.join(self.models_path,'ner-model-2018.12.18.tar.gz'))
           ))
       self.add(Model(
           name = 'textual_entailment',
           displayName = 'decomposable-attention-elmo-2018.02.19.tar.gz',
           description = 'Reimplementation of the decomposable attention model (Parikh et al, 2017)',
           size = '665MB',
           downloader = AllennlpDownloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/decomposable-attention-elmo-2018.02.19.tar.gz',
               path=os.path.join(self.models_path,'decomposable-attention-elmo-2018.02.19.tar.gz'))
           ))
       self.add(Model(
           name = 'coreference_resolution',
           displayName = 'coref-model-2018.02.05.tar.gz',
           description = 'Implementation is based on End-to-End Coreference Resolution (Lee et al, 2017)',
           size = '57MB',
           downloader = AllennlpDownloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/coref-model-2018.02.05.tar.gz',
               path=os.path.join(self.models_path,'coref-model-2018.02.05.tar.gz'))
           ))
       self.add(Model(
           name = 'semantic_role_labeling',
           displayName = 'srl-model-2018.05.25.tar.gz',
           description = 'Reimplementation of a deep BiLSTM model (He et al, 2017)',
           size = '697MB',
           downloader = AllennlpDownloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz',
               path=os.path.join(self.models_path,'srl-model-2018.05.25.tar.gz'))
           ))
       self.add(Model(
           name = 'constituency_parsing',
           displayName = 'elmo-constituency-parser-2018.03.14.tar.gz',
           description = 'Independent scoring of labels and spans from Minimal Span Based Constituency Parser (Stern et al, 2017)',
           size = '677MB',
           downloader = AllennlpDownloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/elmo-constituency-parser-2018.03.14.tar.gz',
               path=os.path.join(self.models_path,'elmo-constituency-parser-2018.03.14.tar.gz'))
           ))
       self.add(Model(
           name = 'dependency_parsing',
           displayName = 'biaffine-dependency-parser-ptb-2018.08.23.tar.gz',
           description = 'Implementation of a neural model for dependency parsing using biaffine classifiers on top of a bidirectional LSTM based on Deep Biaffine Attention for Neural Dependency Parsing (Dozat, 2017)',
           size = '70MB',
           downloader = AllennlpDownloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/biaffine-dependency-parser-ptb-2018.08.23.tar.gz',
               path=os.path.join(self.models_path,'biaffine-dependency-parser-ptb-2018.08.23.tar.gz'))
           ))
       self.add(Model(
           name = 'open_information_extraction',
           displayName = 'openie-model.2018-08-20.tar.gz',
           description = 'Reimplementation of a deep BiLSTM sequence prediction model (Stanovsky et al., 2018)',
           size = '63MB',
           downloader = AllennlpDownloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/openie-model.2018-08-20.tar.gz',
               path=os.path.join(self.models_path,'openie-model.2018-08-20.tar.gz'))
           ))
       self.add(Model(
           name = 'event2mind',
           displayName = 'event2mind-2018.09.17.tar.gz',
           description = 'Reimplementation of the original Event2Mind neural inference model (Rashkin et al, 2018)',
           size = '52MB',
           downloader = AllennlpDownloader(
               url='https://s3-us-west-2.amazonaws.com/allennlp/models/event2mind-2018.09.17.tar.gz',
               path=os.path.join(self.models_path,'event2mind-2018.09.17.tar.gz'))
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
          
class AllennlpDownloader(Downloader):
   def __init__(self, *args, **kwargs):
        Downloader.__init__(self, *args, **kwargs)

   def on_downloaded(self):
        self.status = 'DownloadingSpacy'
        spacy = Spacy()
        en_core_web_sm_path = os.path.join(spacy.models.models_path, 'en_core_web_sm-2.0.0', 'en_core_web_sm')
        en_core_web_sm_default_path = os.path.join(spacy.models.models_path, 'en_core_web_sm')
        if not spacy.models.is_downloaded('en_core_web_sm-2.0.0') or not os.path.exists(en_core_web_sm_default_path):
            spacy.models.download('en_core_web_sm-2.0.0', wait_for_completion = True)
            shutil.copytree(en_core_web_sm_path, en_core_web_sm_default_path)
        pass
