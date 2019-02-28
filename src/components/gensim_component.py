import os
from gensim.summarization import summarize as gensim_summarize
from gensim.summarization import keywords as gensim_keywords
from services.downloader import Downloader

class Gensim:

    def __init__(self):
        pass

    def summarize(self, text, ratio=None, word_count = None, split = None):
        return {
            "summary": gensim_summarize(text, ratio = ratio, word_count = word_count, split = split),
            "keywords": gensim_keywords(text, ratio = ratio, word_count = word_count, split = split),
            }
