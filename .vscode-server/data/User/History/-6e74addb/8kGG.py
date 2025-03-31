import random

NUM_KEYS = 10
KEY_LENGTH = 50


keys = []

for key in range(NUM_KEYS):
    for char in range(KEY_LENGTH):
        keys.append(random.randbytes(2).decode("utf-8"))

    
    print(keys[key])
