from urllib.request import urlopen
from urllib.parse import urljoin
from re import findall

base_url = 'http://www.pythonchallenge.com/pc/def/'
relative_url = str(2**38) + '.html'
url = urljoin(base_url, relative_url)

with urlopen(url) as response:
    html = response.read().decode('utf-8')
    urls = findall(r"\w+.html", html)
    for relative_url in urls:
        print('Next url: ' + urljoin(base_url, relative_url))
