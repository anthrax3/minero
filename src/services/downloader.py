import urllib.request

status = dict()

class Downloader:
    def __init__(self):
        pass

    def download(self, url, local_path):
        if url in status and status[url]["status"] == 'InProgress':
            return;
        urllib.request.urlretrieve(url, local_path, self.reporthook)

    def get_status(self):
        return status;
        
    def reporthook(self, count, block_size, total_size):
        if int(count * block_size * 100 / total_size) == 100:
            status["asdf"] = dict()