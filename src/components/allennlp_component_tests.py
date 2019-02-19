import unittest
from components.allennlp_component import AllenNlp

class AllenNlpTests(unittest.TestCase):

   def test_machine_comprehension(self):
      sut = AllenNlp()
      doc = sut.machine_comprehension(
          passage = "The Matrix is a 1999 science fiction action film written and directed by The Wachowskis, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano.", 
          question = "Who stars in The Matrix?")
      x = True
      

   def test_named_entity_recognition(self):
      sut = AllenNlp()

      doc = sut.named_entity_recognition(
          sentence = "Did Uriah honestly think he could beat The Legend of Zelda in under three hours?"
      )
      self.assertIsNotNone(doc)

   def test_textual_entailment(self):
      sut = AllenNlp()
      doc = sut.textual_entailment(
         hypothesis="Two women are sitting on a blanket near some rocks talking about politics.",
         premise="Two women are wandering along the shore drinking iced tea."
      )
      self.assertIsNotNone(doc)

   def test_coreference_resolution(self):
      sut = AllenNlp()
      doc = sut.coreference_resolution(
         document="The woman reading a newspaper sat on the bench with her dog."
      )
      self.assertIsNotNone(doc)

   def test_semantic_role_labeling(self):
      sut = AllenNlp()
      r = sut.semantic_role_labeling(
         sentence="Did Uriah honestly think he could beat the game in under three hours?"
      )
      self.assertIsNotNone(doc)

   def test_constituency_parsing(self):
      sut = AllenNlp()
      doc = sut.constituency_parsing(
         sentence="If I bring 10 dollars tomorrow, can you buy me lunch?"
      )
      self.assertIsNotNone(doc)


      