from nlp.components.spacy_component import Spacy
import unittest

class SpacyTests(unittest.TestCase):

   def test_nlp(self):
       sut = Spacy()
       sut.models.download("en_core_web_sm-2.0.0", override = False, wait_for_completion = True)
       result = sut.nlp("en_core_web_sm-2.0.0", "I live in New York");
       print(result)
       self.assertIsNotNone(result["entities"])




