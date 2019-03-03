import os
import traceback
import sys
import logging
from gensim.summarization import summarize as gensim_summarize
from gensim.summarization import keywords as gensim_keywords
from services.downloader import Downloader

logger = logging.getLogger(__name__)

class Gensim:

    def __init__(self):
        pass

    def summarize(self, document, ratio=0.2, word_count = None, split = None):
        try:
            return {
                "summary": gensim_summarize(document, ratio = ratio),#, ratio = ratio, word_count = word_count, split = split),
                "keywords": gensim_keywords(document),#, ratio = ratio, word_count = word_count, split = split),
                }
        except Exception as e:
            logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
            return {"error": str(e)}

