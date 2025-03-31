import os


count = 0
for filename in os.listdir(os.getcwd()):
    if count > 10:
        break

    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        line = f.readline()

        items = line.split("|")

        bank = items[2].split(":")[1]

        print(bank)

        count += 1