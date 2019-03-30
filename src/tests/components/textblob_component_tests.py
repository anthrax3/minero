import unittest
from nlp.components.textblob_component import TextBlob

class TextBlobTests(unittest.TestCase):
     def test_nlp(self):
       sut = TextBlob()
       result = sut.nlp("Thomas A. Anderson is a man living two lives. By day he is an average computer programmer and by night a hacker known as Neo. Neo has always questioned his reality, but the truth is far beyond his imagination. Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government. Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix. As a rebel against the machines, Neo must return to the Matrix and confront the agents: super-powerful computer programs devoted to snuffing out Neo and the entire human rebellion.")
       print(result)
       self.assertIsNotNone(result["tokens"])

     def test_spelling_correction(self):
       sut = TextBlob()
       result = sut.spelling_correction("Thomas A. Anderson is a man leving two lives.")
       self.assertEqual("Thomas A. Anderson is a man living two lives.", result["correct"])

     def test_translate(self):
       sut = TextBlob()
       result = sut.translate("Thomas A. Anderson is an man living two lives.", "es")
       print(result)
       self.assertEqual("Thomas A. Anderson es un hombre que vive dos vidas.", result["translation"])

     def test_detect_language(self):
       sut = TextBlob()
       result = sut.detect_language("Thomas A. Anderson is an man living two lives.",)
       self.assertEqual("en", result["language"])
