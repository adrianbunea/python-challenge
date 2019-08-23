from common import make_url

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
print('Next url: ' + make_url(remove_common_characters(text)))