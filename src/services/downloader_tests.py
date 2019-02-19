import urllib.request
import unittest
import os
from services.downloader import Downloader


class DownloaderTests(unittest.TestCase):

    def test_download(self):
        Downloader().download("https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz", "en_core_web_sm-2.0.0.tar.gz")
        pass



    

