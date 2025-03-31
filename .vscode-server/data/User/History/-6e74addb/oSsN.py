import random
from string import ascii_lowercase, ascii_uppercase, digits


NUM_KEYS = 10
KEY_LENGTH = 50

chars = ascii_lowercase + ascii_uppercase + digits

keys: [str] = [] # type: ignore

for key in range(NUM_KEYS):
    keys.append("")
    for char in range(KEY_LENGTH):
        keys[key] += chars[random.randint(0, len(chars)-1)]

    
text = "["
for key in keys:
    text += "\""+key+"\",\n"

text = text[:-2]+"]"

print(text)
