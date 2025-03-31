from cards import *


USERFILESPATH: str = "/home/blackjack/user_profiles"

ILLEGAL_CHARS = ["/", ".", "**", "||", "\\"]

class UserData:
    name: str
    code: int
    bank: int
    wins: int
    losses: int

    def __init__(self):
        self.name = ""
        self.code = -1
        self.bank = -1
        self.wins = -1
        self.losses = -1


class User:

    hands: [Hand] # type: ignore
    data: UserData
    clientID: str

    def __init__(self):
        self.hands = []
        self.data = UserData()

    def toString(self) -> str:
        text = "Name: "+self.data.name+"\n"+"Bank: "+str(self.data.bank)+"\n"+ \
            "Wins: "+str(self.data.wins)+"\n"+"Losses: "+str(self.data.wins)+"\n"
        return text
        
    def hand2String(self) -> str:
        text = ""
        for hand in self.hands:
            print(hand.totalCards())
            text+=hand.toString(True)+":"+str(hand.bet)+":"+hand.result2String()+"\\"
        return text

    def findUserFile(self, username: str) -> bool:
        try:
            open(USERFILESPATH+"/"+username+".txt",  "r")
        except Exception as e:
            return False
        
        return True
        

    def addHand(self, hand: Hand):
        self.hands.append(hand)

    def removeHand(self, hand: int):
        self.hands.pop(hand)

    def createUserFile(self, username: str, code: int):
        # search for invalid characters in the username
        for char in ILLEGAL_CHARS:
            if username.__contains__(char): raise Exception("Invalid Characters: Username contians invalid characters")

        # ensure the username is not too long
        if len(username) > 20: raise Exception("Invalid Username: Username is too long, try a shorter one")

        # ensure the code is more than four digits
        if len(str(code)) < 4: raise Exception("Invalid Code: Must be four or more digits.\nDon't start the code with zeros")

        try:
            file = open(USERFILESPATH+"/"+username+".txt", "x")
        except Exception as e:
            raise e
        
        file.write("name:"+username+"|"+
                   "code:"+str(code)+"|"+
                   "bank:1000|"+
                   "wins:0|"+
                   "losses:0|"+
                   "pushes:0")
        
        self.data.name = username

        file.close()
        self.updateFromFile()

    def signUserIn(self, username: str, code: int):
        self.data.name = username
        self.updateFromFile()

        if code != self.data.code:
            raise Exception("Invalid Code: Code provided is invalid")

    def updateToFile(self):
        try:
            file = open(USERFILESPATH+"/"+self.data.name+".txt", "w")
        except Exception as e:
            raise e
        
        file.write("name:"+self.data.name+"|"+
                   "code:"+str(self.data.code)+"|"+
                   "bank:"+str(self.data.bank)+"|"+
                   "wins:"+str(self.data.wins)+"|"+
                   "losses:"+str(self.data.losses))
        
        file.close()

    def updateFromFile(self):
        try:
            file = open(USERFILESPATH+"/"+self.data.name+".txt", "r")
        except Exception as e:
            raise e

        fileData = file.readline()

        items = fileData.split("|")

        for item in items:
            itemComps = item.split(":")

            if itemComps[0] == "name":
                self.data.name = itemComps[1]
            elif itemComps[0] == "code":
                self.data.code = int(itemComps[1])
            elif itemComps[0] == "bank":
                self.data.bank = int(itemComps[1])
            elif itemComps[0] == "wins":
                self.data.wins = int(itemComps[1])
            elif itemComps[0] == "losses":
                self.data.losses = int(itemComps[1])
            else:
                raise Exception("Invalid Data: User profile contains invalid data")
            
        file.close()