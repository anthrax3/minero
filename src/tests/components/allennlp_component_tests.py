import unittest
from nlp.components.allennlp_component import AllenNlp

class AllenNlpTests(unittest.TestCase):

   def test_machine_comprehension(self):
      sut = AllenNlp()
      sut.models.download('machine_comprehension', override = False, wait_for_completion = True);
      result = sut.machine_comprehension(
          document = "The Matrix is a 1999 science fiction action film written and directed by The Wachowskis, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano.", 
          question = "Who stars in The Matrix?")
      self.assertEqual('Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano', result['answer'])
      

   def test_named_entity_recognition(self):
      sut = AllenNlp()
      sut.models.download('named_entity_recognition', override = False, wait_for_completion = True);
      result = sut.named_entity_recognition(
          document = "Did Uriah honestly think he could beat The Legend of Zelda in under three hours?"
      )
      print(result)
      self.assertIsNotNone(result['tokens'])

   def test_textual_entailment(self):
      sut = AllenNlp()
      sut.models.download('textual_entailment', override = False, wait_for_completion = True);
      result = sut.textual_entailment(
         hypothesis="Two women are sitting on a blanket near some rocks talking about politics.",
         document="Two women are wandering along the shore drinking iced tea."
      )
      self.assertIsNotNone(result['entailment'])
      self.assertIsNotNone(result['contradiction'])
      self.assertIsNotNone(result['neutral'])

   def test_coreference_resolution(self):
      sut = AllenNlp()
      sut.models.download('coreference_resolution', override = False, wait_for_completion = True);
      result = sut.coreference_resolution(
         document="The woman reading a newspaper sat on the bench with her dog."
      )
      print(result)
      self.assertIsNotNone(result)

   def test_semantic_role_labeling(self):
      sut = AllenNlp()
      sut.models.download('semantic_role_labeling', override = False, wait_for_completion = True);
      result = sut.semantic_role_labeling(
         document="Did Uriah honestly think he could beat the game in under three hours?"
      )
      print(result)
      self.assertIsNotNone(result['verbs'])
      
   def test_constituency_parsing(self):
      sut = AllenNlp()
      sut.models.download('constituency_parsing', override = False, wait_for_completion = True);
      result = sut.constituency_parsing(
         document="If I bring 10 dollars tomorrow, can you buy me lunch?"
      )
      print(result)
      self.assertIsNotNone(result)

   def test_open_information_extraction(self):
      sut = AllenNlp()
      sut.models.download('open_information_extraction', override = False, wait_for_completion = True);
      result = sut.open_information_extraction(
         document="Alex Honnold climbed up a New Jersey skyscraper."
      )
      print(result)
      self.assertIsNotNone(result['verbs'])
      
   def test_dependency_parsing(self):
      sut = AllenNlp()
      sut.models.download('dependency_parsing', override = False, wait_for_completion = True);
      result = sut.dependency_parsing(
         document="James ate some cheese whilst thinking about the play."
      )
      print(result)
      self.assertIsNotNone(result['tokens'])
      


      