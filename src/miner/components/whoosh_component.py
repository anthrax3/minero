import os
import traceback
import sys
import logging
import shutil
from miner.config import whoosh_path
from whoosh import index
from whoosh.filedb.filestore import FileStorage
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh import analysis, fields, index, qparser, query, scoring

logger = logging.getLogger(__name__)
indexes = {}

class Whoosh:

    def __init__(self):
        self._ensure_dir(whoosh_path)
        pass

    def _ensure_dir(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    def _index_dir(self, index_name):
        return os.path.join(whoosh_path,index_name)

    def is_index_exists(self, index_name):
        return index.exists_in(self._index_dir(index_name))

    def create_index(self, index_name, schema = Schema()):
        if not self.is_index_exists(index_name):
            self._ensure_dir(self._index_dir(index_name))
            index.create_in(self._index_dir(index_name), schema=schema)
        return self.open_index(index_name)

    def delete_index(self, index_name):
        if self.is_index_exists(index_name):
            shutil.rmtree(self._index_dir(index_name))

    def open_index(self, index_name):
        if not index_name in indexes:
            indexes[index_name] = index.open_dir(self._index_dir(index_name))
        return indexes[index_name]

    def index_document(self, index_name, document):
        writer = self.open_index(index_name).writer()
        writer.add_document(**document)
        writer.commit()

    def find_all(self, index_name, query = None):
        if query:
            return [x for x in self.open_index(index_name).searcher().documents(**query)]
        else:
            return [x for x in self.open_index(index_name).searcher().documents()]
    
    def find_by_id(self, index_name, id):
        return self.open_index(index_name).searcher().document(id = id)