import threading
import socket
import random

KEYS = ["97556001310353571015864887310298645963720420679221",
"50657293895822865917700674480360671730164667104021",
"37873545865909873398839504018513547221886393148906",
"87426898370777417968908451314075974391823801476536",
"78466279592676447851116488877661616124947233545997",
"13192001091879337393407384852067400143425746201876",
"39398927491495223997557931526802363216254802563910",
"16362776439510027830542823542227877489090072087418",
"62320022085667117192908452002593240073267957305415",
"46356135202262694712346954406325310176432299139792"]

AUTH_SERVER_PORT = 3060
AUTH_SERVER_IP = "192.168.0.181"

class ClientAuth:
    clearedUsers: [] # type: ignore 

    def __init__(self):
        self.clearedUsers = []

        self.s = socket.socket()
        self.s.bind((AUTH_SERVER_IP, AUTH_SERVER_PORT))

        self.initServer()

    def userCleared(self, address):
        for user in self.clearedUsers:
            if user == address: return True

        return False

    def initServer(self):
        self.s.listen(5)

        # create the server thread
        thread = threading.Thread(target=self.server_loop)
        thread.start() 

    def server_loop(self):
        while(True):
            # listen for a user connection
            client_s, address = self.s.accept()

            self.print("User connected with: "+str(address))

            if self.userCleared(address):
                self.print("User already cleared")
                client_s.send("Auth||clear")
                return

            # if the array of cleared clients is large, empty it
            if len(self.clearedUsers) > 25:
                self.clearedUser = []

            thread = threading.Thread(target=self.auth_user, args=(client_s, address, ))
            thread.start()

    def auth_user(self, client_s: socket.socket, address):
        # send user ready message
        client_s.send("Auth||connected||?".encode())
            
        # wait for request for code
        rsp = str(client_s.recv(1024).decode()).split("||")
        if rsp[0] != "Auth" or rsp[1] != "ready":
            client_s.send("Error||Invalid auth packet".encode())
            client_s.close()
            return
        
        # get the client ID
        client_key = rsp[2]
        
        # generate a code
        key, mult = self.generate_key_code()

        client_s.send(("Auth||code||"+str(key+mult)).encode())

        key = self.find_digit(key)
        mult = self.find_digit(mult)

        # get the expected key, multipled
        expected = str(int(KEYS[key])*(mult))

        # wait for response from server
        rsp = str(client_s.recv(1024).decode()).split("||")
        if rsp[0] != "Auth":
            client_s.send("Error||No Security code".encode())
            client_s.close()
            return

        if rsp[1] != expected:
            self.print("Client had invalid security key: "+str(address))
            client_s.send("Error||Invalid security code||Nice try Dan".encode())
            client_s.close()
            return
        

        self.print("Client cleared for play")
        self.clearedUsers.append(client_key)
        client_s.send("Auth||clear".encode())
        client_s.close()
        return


    def generate_key_code(self) -> (int): # type: ignore
        first = random.randint(2, 9)

        second = random.randint(1, first-1)

        first = 1 << first
        second = 1 << second
        
        return (first, second)
    
    def find_digit(self, num: int) -> int:
        for i in range(10):
            if num == 1:
                return i
            
            num = num >> 1


    def print(self, str):
        print("Auth Server: "+str)