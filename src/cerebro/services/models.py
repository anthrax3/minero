from cerebro.config import models_path

class Model:
   def __init__(self, name, description = None, downloader = None, size = None, displayName = None):
      self.name = name
      self.displayName = displayName
      self.description = description
      self.size = size
      self.downloader = downloader
      self.model = None

class Models:
   def __init__(self):
       self.models = dict()
       self.models_path = models_path

   def add(self , model):
       self.models[model.name] = model

   def exists(self, name):
       return name in self.models

   def load(self, name):
       pass

   def unload(self, name):
       if self.exists(name):
          self.models[name].model = None

   def is_loaded(self, name):
       if name in self.models and self.models[name].model:
           return True
       return False

   def download(self, name):
       if self.exists(name):
          self.models[name].downloader.download()

   def is_downloaded(self, name):
       if self.exists(name):
           return self.models[name].downloader.is_downloaded()
       return False

   def get(self, name):
       if self.exists(name):
          return self.models[name]
       return None

   def validate_and_load(self, name):
       is_valid, error = self.validate(name)
       if not is_valid:
           return is_valid, error
       return self.load(name)
   
   def validate(self, name):     
       if not name:
           return False, 'Model is required'
       if not self.exists(name):
          return False, 'Model ' + name + ' does not exists.'
       if not self.is_loaded(name):
          if not self.is_downloaded(name):
             return False, 'Model ' + name + ' is not downloaded.'
       return True, None

   def get_status_by_name(self, name):
       models = self.get_status()
       return next(x for x in models if x['name'] == name)

   def get_status(self):
       status = []
       for model_name in self.models.keys():
           model = self.models[model_name]
           status.append({
               'name': model_name,
               'displayName' : self.models[model_name].displayName,
               'description' : self.models[model_name].description,
               'size' : self.models[model_name].size,
               'url' : self.models[model_name].downloader.url,
               'is_loaded': self.is_loaded(model_name),
               'is_downloaded': self.is_downloaded(model_name),
               'is_downloading': self.models[model_name].downloader.is_progress,
               'download_status': self.models[model_name].downloader.status,
               'download_percentage': self.models[model_name].downloader.current_percentage,
               'download_error': self.models[model_name].downloader.error
            })
       return status


