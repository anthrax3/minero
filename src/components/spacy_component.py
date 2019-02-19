import spacy
from spacy.util import set_data_path

class Spacy:
   spacy_nlp = None

   def __init__(self):
       set_data_path("models\spacy")
       self.load_model()
       pass
     
   def load_model(self):
       if not Spacy.spacy_nlp:
          Spacy.spacy_nlp = spacy.load('en_core_web_sm-2.0.0')

   def to_spacy(self, text):
       return Spacy.spacy_nlp(text);

   def to_dict(self, text):
       doc_dict = {"entities": [], "tokens": [], "noun_chunks": [], "sentences": []}
       doc_spacy = self.to_spacy(text)
       for token in doc_spacy:
           doc_dict["tokens"].append(
               {
                  "text": token.text,
                  "lemma": token.lemma_,
                  "pos": token.pos_,
                  "tag": token.tag_,
                  "dep_": token.dep_,
                  "shape_,": token.shape_,
                  "is_alpha": token.is_alpha,
                  "is_stop": token.is_stop,
                  "head.tex": token.head.text,
                  "head.pos,": token.head.pos_,
                  "has_vector": token.has_vector, 
                  #"vector_norm": token.vector_norm, 
                  "is_oov": token.is_oov
                  #"children": [child for child in token.children]
               })

       for chunk in doc_spacy.noun_chunks:
          doc_dict["noun_chunks"].append(
              {
                  "text": chunk.text, 
                  "root.text": chunk.root.text,
                  "root.dep_": chunk.root.dep_,
                  "label_": chunk.label_,
                  "root.head.text": chunk.root.head.text
              })

       for sentence in doc_spacy.sents:
          doc_dict["sentences"].append(
              {
                  "text": sentence.text
              })

       for entity in doc_spacy.ents:
          doc_dict["entities"].append(
              {
                  "text": entity.text, 
                  "label_": entity.label_,
                  "start_char": entity.start_char, 
                  "end_char": entity.end_char
              })

           
       return doc_dict
