import os
import traceback
import sys
import logging
import shutil
import uuid
from miner.config import whoosh_path
from whoosh import index
from whoosh.filedb.filestore import FileStorage
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED, UnknownFieldError
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

    def _ensure_id_field(self, index_name):
        with self.open_index(index_name).writer() as w:
            w.add_field("id", fields.ID(unique=True, stored=True))

    def _ensure_fields(self, index_name, document):
        with self.open_index(index_name).writer() as w:
            for field_name in document:
                if field_name not in w.schema:
                    w.add_field(field_name, fields.TEXT(stored=True))

    def create_index(self, index_name, schema = Schema()):
        if not self.is_index_exists(index_name):
            self._ensure_dir(self._index_dir(index_name))
            index.create_in(self._index_dir(index_name), schema=schema)
            self._ensure_id_field(index_name)
        return self.open_index(index_name)

    def delete_index(self, index_name):
        if self.is_index_exists(index_name):
            shutil.rmtree(self._index_dir(index_name))

    def open_index(self, index_name):
        if not index_name in indexes:
            indexes[index_name] = index.open_dir(self._index_dir(index_name))
        return indexes[index_name]

    def index_document(self, index_name, document):
        try:
            if not "id" in document:
                document["id"] = str(uuid.uuid4())
            w = self.open_index(index_name).writer()
        except index.EmptyIndexError as e:
            self.create_index(index_name)
            w = self.open_index(index_name).writer()

        try:
            w.update_document(**document)
            w.commit()
        except UnknownFieldError as e:
            w.cancel()
            self._ensure_fields(index_name, document)
            with self.open_index(index_name).writer() as w2:
                w2.update_document(**document)

    def delete_document(self, index_name, id):
        with self.open_index(index_name).writer() as w:
            w.delete_by_term("id", id)
        

    def find_all(self, index_name, query = None):
        if query:
            return [x for x in self.open_index(index_name).searcher().documents(**query)]
        else:
            return [x for x in self.open_index(index_name).searcher().documents()]
    
    def find_by_id(self, index_name, id):
        return self.open_index(index_name).searcher().document(id = id)