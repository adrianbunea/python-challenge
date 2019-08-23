from urllib.parse import urljoin

def read_file(filename):
    file = open(filename ,"r")
    if file.mode == 'r':
        return file.read()

def remove_common_characters(text):
    common_characters = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '[', ']', '{', '}', '\n', '' ]
    for character in common_characters:
        text = text.replace(character, '')
    return text

text = read_file("find-the-rare-characters.txt")
base_url = 'http://www.pythonchallenge.com/pc/def/'
relative_url = remove_common_characters(text) + '.html'
print('Next url: ' + urljoin(base_url, relative_url))