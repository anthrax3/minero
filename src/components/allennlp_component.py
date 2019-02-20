from allennlp.predictors.predictor import Predictor

class AllenNlp(object):
   machine_comprehension_model = None
   named_entity_recognition_model = None
   textual_entailment_model = None
   coreference_resolution_model = None
   constituency_parsing_model = None
   semantic_role_labeling_model = None

   def machine_comprehension(self, passage, question):
      #predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")
      if not AllenNlp.machine_comprehension_model:
         AllenNlp.machine_comprehension_model = Predictor.from_path("C:\\Projects\\nlp\\src\\models\\allennlp\\bidaf-model-2017.09.15-charpad.tar.gz")
      prediction =  AllenNlp.machine_comprehension_model.predict(
         passage = passage,
         question = question
      )
      return prediction

   def named_entity_recognition(self, sentence):
      #predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/ner-model-2018.12.18.tar.gz")
      if not AllenNlp.named_entity_recognition_model:
         AllenNlp.named_entity_recognition_model = Predictor.from_path("C:\\Projects\\nlp\\src\\models\\allennlp\\ner-model-2018.12.18.tar.gz")
      prediction =  AllenNlp.named_entity_recognition_model.predict(
         sentence = sentence
      )
      return prediction

   def textual_entailment(self, hypothesis, premise):
      #predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/decomposable-attention-elmo-2018.02.19.tar.gz")
      if not AllenNlp.textual_entailment_model:
         AllenNlp.textual_entailment_model = Predictor.from_path("C:\\Projects\\nlp\\src\\models\\allennlp\\decomposable-attention-elmo-2018.02.19.tar.gz")
      prediction =  AllenNlp.textual_entailment_model.predict(
         hypothesis = hypothesis,
         premise = premise
      )
      return prediction

   def coreference_resolution(self, document):
      #predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/coref-model-2018.02.05.tar.gz")
      if not AllenNlp.coreference_resolution_model:
         AllenNlp.coreference_resolution_model = Predictor.from_path("C:\\Projects\\nlp\\src\\models\\allennlp\\coref-model-2018.02.05.tar.gz")
      prediction =  AllenNlp.coreference_resolution_model.predict(
         document = document
      )
      return prediction

   def semantic_role_labeling(self, sentence):
      #predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/srl-model-2018.05.25.tar.gz")
      if not AllenNlp.semantic_role_labeling_model:
         AllenNlp.semantic_role_labeling_model = Predictor.from_path("C:\\Projects\\nlp\\src\\models\\allennlp\\srl-model-2018.05.25.tar.gz")
      prediction =  AllenNlp.semantic_role_labeling_model.predict(
         sentence = sentence
      )
      return prediction

   def constituency_parsing(self, sentence):
      #predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/elmo-constituency-parser-2018.03.14.tar.gz")
      if not AllenNlp.constituency_parsing_model:
          AllenNlp.constituency_parsing_model = Predictor.from_path("C:\\Projects\\nlp\\src\\models\\allennlp\\elmo-constituency-parser-2018.03.14.tar.gz")
      prediction =  AllenNlp.constituency_parsing_model.predict(
         sentence = sentence
      )
      return prediction
