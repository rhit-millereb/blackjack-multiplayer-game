import threading
import socket
from user import UserData
import os
from server import Client

USER_FOLDER_PATH = "/home/blackjack/user_profiles"

IP = "192.168.0.181"
PORT = 3080

class LeaderboardServer:
    clientIDs: [str] # type: ignore

    data: [UserData] # type: ignore

    # array of all data 0=highest bank, len()-1 = lowest
    namesBankOrder: [UserData] # type: ignore

    # array of all data 0=most wins, len()-1 = least wins
    totalWinsOrder: [UserData] # type: ignore

    # array of string concat of username|winrate, first=highest, last=lowest
    winRateOrder: [str] # type: ignore

    server: socket.socket
    connections: [] # type: ignore

    def __init__(self, clientIDs):
        self.data = []
        self.namesBankOrder = []
        self.totalWinsOrder = []
        self.winRateOrder = []
        self.connections = []

        self.clientIDs = clientIDs

        self.calculateAllData()

        self.server = socket.socket()
        self.server.bind((IP, PORT))

        self.initServer()


    def initServer(self):
        self.server.listen(5)

        # create thread to listen for connections
        thread = threading.Thread(target=self.serverLoop)
        thread.start()


    def serverLoop(self):
        while True:
            client, address = self.server.accept()

            self.print("User connected with address: "+str(address))

            thread = threading.Thread(target=self.userMessage, args=(client, address, ))
            thread.start()

    def userMessage(self, client: socket.socket, address):
        # send message to client stating leaderboard connected
        client.send("Lead||connected".encode())

        # get response from client with client ID
        rsp = client.recv(1024).decode().split("||")
        if len(rsp) != 2 or rsp[0] != "Lead":
            client.send("Error||Invalid user response")
            client.close()
            self.print("User gave invalid response: "+address)
            return
        
        clientID = rsp[1]

        client.send("")


    def getUserNameFromID(self, id) -> str:
        for client in self.clients:
            if client.clientID == id:
                return client.name
            
        raise Exception("No user found with ID: "+id)

    def calculateAllData(self):
        self.getBankOrder()
        self.getWinOrder()
        self.getWinRateOrder()

    def getBankOrder(self):
        data = list(self.data)

        for i in range(len(data)):
            temp: UserData = UserData()
            for item in data:
                if item.bank > temp.bank:
                    temp = item
            data.remove(temp)
            self.namesBankOrder.append(temp)


    def getWinOrder(self):
        data = list(self.data)

        for i in range(len(data)):
            temp: UserData = UserData()
            for item in data:
                if item.wins > temp.wins:
                    temp = item
            data.remove(temp)
            self.totalWinsOrder.append(temp)


    def getWinRateOrder(self):
        winRates = {}

        for item in self.data:
            rate = float(item.wins) / float(item.wins+item.pushes+item.losses)

            winRates[item.name] = float(rate)

        for i in range(len(winRates)):
            temp = -1
            name = ""
            for key, item in winRates.items():
                if item > temp:
                    temp = item
                    name = key

            winRates.pop(name)

            self.winRateOrder.append(name+":"+str(temp))


    def getAllData(self):
        for filename in os.listdir(USER_FOLDER_PATH):
            # skip utilities files
            if filename == "_removalOutput.txt" or filename == "_removeLargeBanks.py":
                continue

            with open(os.path.join(USER_FOLDER_PATH, filename), 'r') as f:
                # create an instance of user data
                userData: UserData = UserData()

                line = f.readline()
                data = line.split("|")

                for item in data:
                    items = item.split(":")

                    if items[0] == "name":
                        userData.name = items[1]
                    elif items[0] == "bank":
                        userData.bank = int(items[1])
                    elif items[0] == "wins":
                        userData.wins = int(items[1])
                    elif items[0] == "losses":
                        userData.losses = int(items[1])
                    elif items[0] == "pushes":
                        userData.pushes = int(items[1])
                
                self.data.append(userData)
        
        self.print("Updated all data on users")


    def print(self, msg):
        print("Leaderboard: "+str(msg)) 