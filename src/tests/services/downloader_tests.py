import unittest
from nlp.services.downloader import Downloader
import os

url = "https://raw.githubusercontent.com/golabek-io/nlp/master/README.md"
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")

class DownloaderTests(unittest.TestCase):

   def test_download_file(self):
        if os.path.exists(path):
            os.remove(path)

        task = Downloader(
            url = url, 
            path = path, 
            overwrite = True)
        
        task.download() 
        task.wait();
        self.assertEqual("Completed", task.status)
        self.assertTrue(os.path.exists(path))

   def test_is_downloaded(self):
        if os.path.exists(path):
            os.remove(path)

        task = Downloader(
            url = url, 
            path = path, 
            overwrite = True)
        
        self.assertFalse(task.is_downloaded())
        task.download() 
        task.wait();
        self.assertTrue(task.is_downloaded())

   def test_download_with_error(self):
        if os.path.exists(path):
            os.remove(path)

        task = Downloader(
            url = "https://adsf/asdf/asdf", 
            path = path, 
            overwrite = True)
        
        task.download() 
        task.wait();
        self.assertEqual("Error", task.status)


