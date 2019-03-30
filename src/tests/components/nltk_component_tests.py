import unittest
from nlp.components.nltk_component import Nltk

class NltkTests(unittest.TestCase):

     def test_neutral_vader_sentiment_analysis(self):
       sut = Nltk()
       result = sut.vader_sentiment_analysis("Thomas A. Anderson is a man living two lives.")
       print(result)
       self.assertEqual(0, result["sentiment"]["negative"])
       self.assertEqual(1, result["sentiment"]["neutral"])
       self.assertEqual(0, result["sentiment"]["positive"])

     def test_negative_vader_sentiment_analysis(self):
       sut = Nltk()
       result = sut.vader_sentiment_analysis("I hate New York")
       print(result)
       self.assertEqual(0.649, result["sentiment"]["negative"])
       self.assertEqual(0.351, result["sentiment"]["neutral"])
       self.assertEqual(0, result["sentiment"]["positive"])

     def test_positive_vader_sentiment_analysis(self):
       sut = Nltk()
       result = sut.vader_sentiment_analysis("I love New York")
       print(result)
       self.assertEqual(0, result["sentiment"]["negative"])
       self.assertEqual(0.323, result["sentiment"]["neutral"])
       self.assertEqual(0.677, result["sentiment"]["positive"])


