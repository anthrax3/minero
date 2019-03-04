import unittest
from downloader import Downloader


task = Downloader()
task.download("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz", "C:\\Projects\\prophet\\bidaf-model-2017.09.15-charpad.tar.gz", overwrite = True, unzip = True) 
print(task.status)
task.wait();
print(task.status)
x = 0;

