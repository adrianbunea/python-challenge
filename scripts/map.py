from urllib.request import urlopen
from urllib.parse import urljoin
from string import ascii_lowercase

def caesar_cipher(text, shift):
    translation_table = make_translation_table(shift)
    return text.translate(translation_table)

def make_translation_table(shift):
    alphabet = ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return ''.maketrans(alphabet, shifted_alphabet)

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(caesar_cipher(text, 2))

base_url = 'http://www.pythonchallenge.com/pc/def/'
relative_url = caesar_cipher('map', 2) + '.html'
print('Next url: ' + urljoin(base_url, relative_url))