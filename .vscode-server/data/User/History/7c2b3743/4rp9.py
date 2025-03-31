import os


count = 0
for filename in os.listdir(os.getcwd()):
    if count > 10:
        break

    remove = False
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        line = f.readline()

        items = line.split("|")

        name = items[0].split(":")[1]
        bank = items[2].split(":")[1]

        if int(bank) > 10000 or int(bank) < 0:
            print(name+" has illegal bank: "+bank)
            remove = True
        else:
            print(name+" has legal bank!")

        count += 1