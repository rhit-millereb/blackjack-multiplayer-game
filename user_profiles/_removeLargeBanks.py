import os


count = 0
for filename in os.listdir(os.getcwd()):

    # do not iterate this file
    if filename == "_removeLargeBanks.py" or filename == "_removalOutput.txt":
        continue

    remove = False
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        line = f.readline()

        items = line.split("|")

        name = items[0].split(":")[1]
        bank = items[2].split(":")[1]

        if int(bank) > 100000 or int(bank) < 0:
            print(name+" has illegal bank: "+bank)
            remove = True
        elif int(bank) == 0:
            print(name+" is out of money")
            remove = True
        else:
            print(name+" LEGAL bank: "+bank)
    
    if remove:
        print("Removing: "+name+"  >"+line)
        os.remove(filename)
        count += 1


print("Removed "+str(count)+" accounts!")
