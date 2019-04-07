import unittest
from miner.components.crawler_component import Crawler

class CrawlerTests(unittest.TestCase):
     def test_medium_homepage(self):
         sut = Crawler()
         medium = sut.parse("https://medium.com")
         self.assertIsNotNone(medium)
         self.assertTrue(medium["html"].startswith("<!DOCTYPE html><html"))
         self.assertTrue(len(medium["links"]) > 0)
         self.assertTrue(medium["scroll_count"] >= 1)

     def test_medium_profile_latest(self):
         sut = Crawler()
         medium = sut.parse("https://medium.com/@nishparadox/latest")
         self.assertIsNotNone(medium)
         self.assertTrue(medium["html"].startswith("<!DOCTYPE html><html"))
         self.assertTrue(len(medium["links"]) > 0)
         self.assertTrue(medium["scroll_count"] >= 5)     
