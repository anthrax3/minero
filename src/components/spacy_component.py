import os
import tarfile
import shutil
import spacy
from spacy.util import set_data_path
from services.downloader import Downloader

class Spacy:
   models = dict()
   models['en_core_web_sm-2.0.0'] = {'description': 'English	Vocabulary, syntax, entities'}
   models['en_core_web_md-2.0.0'] = {'description': 'English	Vocabulary, syntax, entities, vectors'}
   models['en_core_web_lg-2.0.0'] = {'description': 'English	Vocabulary, syntax, entities, vectors'}
   models['en_vectors_web_lg-2.0.0'] = {'description': 'English	Word vectors'}
   models['de_core_news_sm-2.0.0'] = {'description': 'German	Vocabulary, syntax, entities'}
   models['es_core_news_sm-2.0.0'] = {'description': 'Spanish	Vocabulary, syntax, entities'}
   models['es_core_news_md-2.0.0'] = {'description': 'Spanish	Vocabulary, syntax, entities, vectors'}
   models['pt_core_news_sm-2.0.0'] = {'description': 'Portuguese	Vocabulary, syntax, entities'}
   models['fr_core_news_sm-2.0.0'] = {'description': 'French	Vocabulary, syntax, entities'}
   models['fr_core_news_md-2.0.0'] = {'description': 'French	Vocabulary, syntax, entities, vectors'}
   models['it_core_news_sm-2.0.0'] = {'description': 'Italian	Vocabulary, syntax, entities'}
   models['nl_core_news_sm-2.0.0'] = {'description': 'Dutch	Vocabulary, syntax, entities'}
   models['xx_ent_wiki_sm-2.0.0'] = {'description': 'Multi-language	Named entities'}

   def __init__(self):
       set_data_path("models\spacy")
       pass
       
   def nlp(self, model, text):
       if not self.is_model_exists(model):
          return {'error': 'Model ' + model + ' does not exists.'}
       if not self.is_model_loaded(model):
          if not self.is_model_downlaoded(model):
             return {'error': 'Model ' + model + ' is not downloaded.'}
          else:
             self.load_model(model)
       doc_spacy = Spacy.models[model]['model'](text)
       doc_dict = {"entities": [], "tokens": [], "noun_chunks": [], "sentences": []}
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

   def is_model_exists(self, model):
       return model in Spacy.models

   def is_model_loaded(self, model):
       return model in Spacy.models and 'model' in Spacy.models[model]

   def is_model_downlaoded(self, model):
       downloaded_models = os.listdir('C:\\Projects\\nlp\\src\\models\\spacy')
       return model in downloaded_models

   def load_model(self, model):
       if model in Spacy.models and 'model' not in Spacy.models[model]:
             Spacy.models[model]['model'] = spacy.load(model)

   def unload_model(self, model):
       if model in Spacy.models:
          del (Spacy.models[model])['model']

   def download_model(self, model):
       if model in Spacy.models:
           Spacy.models[model]['downloader'] = SpacyDownloader()
           Spacy.models[model]['downloader'].download(
                'https://github.com/explosion/spacy-models/releases/download/{}/{}.tar.gz'.format(model, model),
                'C:\\Projects\\nlp\\src\\models\\spacy\\{}.tar.gz'.format(model),
                overwrite=True)
   def get_model_status_by_name(self, model):
       models = self.get_model_status()
       return next(x for x in models if x['name'] == model)

   def get_model_status(self):
       status = []
       for model_name in Spacy.models.keys():
           model = Spacy.models[model_name]
           status.append({
               'name': model_name,
               'description' : model['description'],
               'is_loaded': self.is_model_loaded(model_name),
               'is_downloaded': self.is_model_downlaoded(model_name),
               'is_downloading': model['downloader'].is_progress if 'downloader' in model else False,
               'download_status': model['downloader'].status if 'downloader' in model else None,
               'download_percentage': model['downloader'].current_percentage if 'downloader' in model else None,
               'download_error': model['downloader'].error if 'downloader' in model else None
            })
       return status


class SpacyDownloader(Downloader):
    def on_downloaded(self, file_url, dest_path, overwrite):
        self.status = 'ExtractingArchive'
        destination_directory, destination_file = os.path.split(dest_path)
        model_name_with_version = destination_file.split('.tar.gz')[0]
        model_name_without_version = destination_file.split('-')[0]
        try:
            #remove exisisting extraction
            extraction_path = os.path.join(destination_directory,model_name_without_version)
            shutil.rmtree(extraction_path, ignore_errors=True)
            #extract
            if dest_path.endswith('tar.gz'):
               with tarfile.open(dest_path, 'r:gz') as tar:
                  tar.extractall(destination_directory)
        except Exception as e:
            self.status = 'Error'
            self.error = 'Error durring extracting archive: ' + str(e)
            return

        try:
            #move
            move_from = os.path.join(destination_directory,model_name_with_version,model_name_without_version)
            move_to = os.path.join(destination_directory)
            shutil.move(move_from, move_to);
        except Exception as e:
            self.status = 'Error'
            self.error = 'Error durring moving extracted archive: ' + str(e)
            return

        try:
            #rename
            rename_from = os.path.join(destination_directory,model_name_without_version)
            rename_to = os.path.join(destination_directory,model_name_with_version)
            shutil.rmtree(rename_to, ignore_errors=True)
            os.rename(rename_from, rename_to)
        except Exception as e:
            self.status = 'Error'
            self.error = 'Error durring renaming extracted archive: ' + str(e)
            return
        
        self.status = 'ExtractedArchive'
        pass
