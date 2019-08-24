import re
from common import make_url, read_file

text = read_file("resources/three-big-bodyguards.txt")
pattern = r"(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])"
hint = ''.join(re.findall(pattern, text))

print("Next url: " + make_url(hint))