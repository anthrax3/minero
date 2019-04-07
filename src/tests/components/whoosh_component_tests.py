import unittest
from miner.components.whoosh_component import Whoosh
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.compat import b, u, text_type

class WhooshTests(unittest.TestCase):
     def test_create_delete(self):
         sut = Whoosh()
         sut.create_index("create_delete")
         self.assertTrue(sut.is_index_exists("create_delete"))
         sut.delete_index("create_delete")
         self.assertFalse(sut.is_index_exists("create_delete"))

     def test_add_document_find_by_id(self):
         sut = Whoosh()
         sut.delete_index("test")
         sut.create_index("test", schema = Schema(id=ID(stored=True),name=TEXT(stored=True)))

         sut.index_document("test", {'id':'1', 'name':'Daniel'});
         document = sut.find_by_id("test", '1')
         
         self.assertEqual('1', document['id'])
         self.assertEqual('Daniel', document['name'])

         sut.delete_index("test")

     def test_add_documents_find_by_field(self):
         sut = Whoosh()
         sut.delete_index("test")
         sut.create_index("test", schema = Schema(id=ID(stored=True),name=TEXT(stored=True)))

         sut.index_document("test", {'id':'1', 'name':u("Daniel")});
         sut.index_document("test", {'id':'2', 'name':u("Jon")});
         
         documents = [x for x in sut.find_all("test", {'name':u("jon")})]
         
         self.assertEqual('2', documents[0]['id'])
         self.assertEqual('Jon', documents[0]['name'])

         sut.delete_index("test")

     def test_add_documents_find_all(self):
         sut = Whoosh()
         sut.delete_index("test")
         sut.create_index("test", schema = Schema(id=ID(stored=True),name=TEXT(stored=True)))

         sut.index_document("test", {'id':'1', 'name':'Daniel'});
         sut.index_document("test", {'id':'2', 'name':'Jon'});
         
         documents = [x for x in sut.find_all("test")]
         
         self.assertEqual('1', documents[0]['id'])
         self.assertEqual('Daniel', documents[0]['name'])

         self.assertEqual('2', documents[1]['id'])
         self.assertEqual('Jon', documents[1]['name'])

         sut.delete_index("test")

