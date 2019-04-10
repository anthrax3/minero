import unittest
from miner.components.whoosh_component import Whoosh
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.compat import b, u, text_type
from whoosh.writing import IndexWriter
class LockTest(IndexWriter):
    def __init__(self):
        pass
    

class WhooshTests(unittest.TestCase):
     def test_create_and_delete_index(self):
         sut = Whoosh()
         sut.create_index("create_delete")
         self.assertTrue(sut.is_index_exists("create_delete"))
         sut.delete_index("create_delete")
         self.assertFalse(sut.is_index_exists("create_delete"))

     def test_add_document(self):
         sut = Whoosh()
         sut.delete_index("test")
         sut.create_index("test", schema = Schema(id=ID(stored=True),name=TEXT(stored=True)))

         sut.index_document("test", {'id':'1', 'name':'Daniel'});
         
         documents = [x for x in sut.find_all("test")]
         
         self.assertEqual(1, len(documents))
         self.assertEqual('1', documents[0]['id'])
         self.assertEqual('Daniel', document[0]['name'])

         sut.delete_index("test")

     def test_find_by_id(self):
         sut = Whoosh()
         sut.delete_index("test")
         sut.create_index("test", schema = Schema(id=ID(stored=True),name=TEXT(stored=True)))

         sut.index_document("test", {'id':'1', 'name':'Daniel'});
         document = sut.find_by_id("test", '1')
         
         self.assertEqual('1', document['id'])
         self.assertEqual('Daniel', document['name'])

         sut.delete_index("test")

         
     def test_add_document_with_extending_schema(self):
         with LockTest() as t:
             x = 0
         sut = Whoosh()
         sut.delete_index("test")
         sut.create_index("test")

         sut.index_document("test", {'id':'1', 'name':'Daniel'});
         document = sut.find_by_id("test", '1')
         
         self.assertEqual('1', document['id'])
         self.assertEqual('Daniel', document['name'])

         sut.delete_index("test")

     def test_add_document_with_creating_new_index(self):
         with LockTest() as t:
             x = 0
         sut = Whoosh()
         sut.delete_index("test")

         sut.index_document("test", {'id':'1', 'name':'Daniel'});
         document = sut.find_by_id("test", '1')
         
         self.assertEqual('1', document['id'])
         self.assertEqual('Daniel', document['name'])

         sut.delete_index("test")

     def test_find_by_field(self):
         sut = Whoosh()
         sut.delete_index("test")
         sut.create_index("test", schema = Schema(id=ID(stored=True),name=TEXT(stored=True)))

         sut.index_document("test", {'id':'1', 'name':u("Daniel")});
         sut.index_document("test", {'id':'2', 'name':u("Jon")});
         
         documents = [x for x in sut.find_all("test", {'name':u("jon")})]
         
         self.assertEqual('2', documents[0]['id'])
         self.assertEqual('Jon', documents[0]['name'])

         sut.delete_index("test")

     def test_find_all(self):
         sut = Whoosh()
         sut.delete_index("test")
         sut.create_index("test", schema = Schema(id=ID(stored=True),name=TEXT(stored=True)))

         sut.index_document("test", {'id':'1', 'name':'Daniel'});
         sut.index_document("test", {'id':'2', 'name':'Jon'});
         
         documents = [x for x in sut.find_all("test")]
         
         self.assertEqual(2, len(documents))
         self.assertEqual('1', documents[0]['id'])
         self.assertEqual('Daniel', documents[0]['name'])
         self.assertEqual('2', documents[1]['id'])
         self.assertEqual('Jon', documents[1]['name'])

         sut.delete_index("test")


     def test_delete_documents(self):
         sut = Whoosh()
         sut.delete_index("test")

         sut.index_document("test", {'id':'1', 'name':'Daniel'});
         sut.index_document("test", {'id':'2', 'name':'Jon'});
         
         sut.delete_document("test", '1')

         documents = [x for x in sut.find_all("test")]
         
         self.assertEqual(1, len(documents))
         self.assertEqual('2', documents[0]['id'])
         self.assertEqual('Jon', documents[0]['name'])

         sut.delete_index("test")

     def test_update_documents(self):
         sut = Whoosh()
         sut.delete_index("test")

         sut.index_document("test", {'id':'1', 'name':'Daniel'});
         sut.index_document("test", {'id':'2', 'name':'Jon'});
         
         #update
         sut.index_document("test", {'id':'1', 'name':'Daniel Paul'});

         documents = [x for x in sut.find_all("test")]
         
         self.assertEqual(2, len(documents))
         self.assertEqual('2', documents[0]['id'])
         self.assertEqual('Jon', documents[0]['name'])
         self.assertEqual('1', documents[1]['id'])
         self.assertEqual('Daniel Paul', documents[1]['name'])

         sut.delete_index("test")
