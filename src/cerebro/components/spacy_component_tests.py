from components.spacy_component import Spacy
import unittest

class SpacyTests(unittest.TestCase):
   def test_to_spacy(self):
       sut = Spacy()
       spacy_model = sut.to_spacy("I live in New York");
       self.assertIsNotNone(spacy_model)

   def test_to_dict(self):
       sut = Spacy()
       dict_model = sut.to_dict("I live in New York");
       self.assertIsNotNone(dict_model)



