from cards import *


USERFILESPATH: str = "/home/blackjack/user_profiles"


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

    def __init__(self, username: str, code: int):
        self.hands = []
        self.data = UserData()

        # find if the user exists
        if not self.findUserFile(username):
            self.createUserFile(username, code)
        else:
            self.signUserIn(username, code)

    def toString(self) -> str:
        print("Name: "+self.data.name+"\n"+
              "Bank: "+str(self.data.bank)+"\n"+
              "Wins: "+str(self.data.wins)+"\n"+
              "Losses: "+str(self.data.wins)+"\n")

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
        if (username.__contains__(":") or username.__contains__("|")): raise Exception("Invalid Characters: Cannot use \':\' or \'|\' in username")

        try:
            file = open(USERFILESPATH+"/"+username+".txt", "x")
        except Exception as e:
            raise e
        
        file.write("name:"+username+"|"+
                   "code:"+str(code)+"|"+
                   "bank:0|"+
                   "wins:0|"+
                   "losses:0")
        
        self.data.username = username

        file.close()
        self.updateFromFile()

    def signUserIn(self, username: str, code: int):
        self.data.username = username
        self.updateFromFile()

        if code != self.data.code:
            raise Exception("Invalid Code: Code provided is invalid")

    def updateToFile(self):
        try:
            file = open(USERFILESPATH+"/"+self.data.username+".txt", "w")

    def updateFromFile(self):
        try:
            file = open(USERFILESPATH+"/"+self.data.username+".txt", "r")
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