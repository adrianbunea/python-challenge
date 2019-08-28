from urllib.request import urlopen
import re
from common import make_url

def follow_the_chain(html):
    pattern = r'(?<=(next nothing is ))[0-9]+'
    matches = re.search(pattern, html)
    while matches:
        next_number = int(matches[0])
        html = get_html(next_number)
        matches = re.search(pattern, html)
    return next_number

def get_html(number):
    next_url = make_url('linkedlist.php?nothing=' + str(number))
    html = urlopen(next_url).read().decode('utf-8')
    print(html)
    return html


html = get_html(12345)
number = follow_the_chain(html)    
html = get_html(number/2)
follow_the_chain(html)