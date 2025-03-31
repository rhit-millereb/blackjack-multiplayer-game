import random
from string import ascii_lowercase, ascii_uppercase, digits


NUM_KEYS = 10
KEY_LENGTH = 50

chars = ascii_lowercase + ascii_uppercase + digits

keys = []

for key in range(NUM_KEYS):
    keys.append("")
    for char in range(KEY_LENGTH):
        keys[key] += chars[random.randint(0, len(chars)-1)]

    

print("["+keys.join(",\n")+"]")
