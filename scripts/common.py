from urllib.parse import urljoin

def make_url(text):
    base_url = 'http://www.pythonchallenge.com/pc/def/'
    relative_url = text + '.html'
    return urljoin(base_url, relative_url)

def read_file(filename):
    file = open(filename ,"r")
    if file.mode == 'r':
        return file.read()