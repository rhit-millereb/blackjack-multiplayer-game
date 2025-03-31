import socket
from threading import Thread
from threading import Event
from settings import Settings
from user import User
from auth import ClientAuth
from chat import Chat
import time

KEY = "qlABCOT3cEpqStkhFhiT1Zg7xjolhFnp"
#"55CVPIUX8W13GWBUVIIPGLANPF"

class Client:

    name: str
    ip: str
    message: str
    s: socket
    code: int

    def __init__(self, name: str, ip: str, s: socket):
        self.name = name
        self.ip = ip
        self.s = s

    def toString(self) -> str:
        return "Name: "+self.name+"  IP: "+str(self.ip)

    def userAccountExists(self) -> bool:
        return User().findUserFile(self.name)

    def createUserAccount(self, code: int) -> bool:
        try:
            User().createUserFile(self.name, code)
        except Exception as e:
            print(e)
            return False
        
        self.code = code
        return True

    def signInAccount(self, code: int) -> bool:
        try:
            User().signUserIn(self.name, code)
        except Exception as e:
            print(e)
            return False
        
        self.code = code
        return True

    timer: int
    kill: bool
    stop: bool = False
    message: str = None
    def askQuestion(self, msg: str, rsp: str = None, i: int = None, timeout: int = None) -> str:
        self.timer = 0
        self.kill = False
        self.stop = False
        self.message = None

        # set the default timeout to 30
        if timeout is None:
            timeout = 30

        # in a sperate thread, handle waiting for a response
        thread = Thread(target=self._handleAskingQuestion, args=(msg, ))
        thread.start()

        # start the timer thread
        timer = Thread(target=self._killTimer, args=(timeout, ))
        timer.start()

        while(self.message is None and not self.kill):
            time.sleep(0.01)
        
        self.stop = True

        if self.kill:
            print(self.name+" response timeout")
            rsp[i] = "timeout"
            raise Exception("Error: No user response (timeout)")

        # determine if function can return value (no if a mutable object was given)
        if rsp is None:
            return self.message
        elif i is None:
            rsp = self.message
            return
        else:
            rsp[i] = self.message


    def _handleAskingQuestion(self, msg: str):
        self.sendMessage(msg)
        self.message = self.waitForMessage()
        return
    
    def _killTimer(self, timeout: int):
        while True:
            time.sleep(1)
            # print("Kill timer: "+str(self.timer))
            if self.timer == timeout:
                self.kill = True
                try:
                    self.sendMessage("timeout")
                except Exception as e:
                    pass
                return
            if self.stop:
                return

            self.timer += 1
        

    def sendMessage(self, msg: str):
        self.s.send((msg+"**").encode())

    def waitForMessage(self) -> str:
        return self.s.recv(2048).decode()

    def close(self):
        self.s.close()

class Server:
    ip: str
    port: str

    waitUsers: bool
    waitThread: Thread
    waitEvent: Event

    settings: Settings

    clients: [Client] # type: ignore
    usersReady: [bool] # type: ignore
    
    waitingUsers: int

    authServer: ClientAuth

    def __init__(self, settings: Settings):
        # init the arrays
        self.clients = []
        self.usersReady = []

        # assign the settings variable
        self.settings = settings

        # init all of the network variables
        self.ip = "192.168.0.181"
        self.port = 3051 #3050
        self.waitUsers = False
        self.waitingUsers = 0
        
        # init the auth server
        self.authServer = ClientAuth()

        # init the server, bind to address and port
        self.s = socket.socket()
        self.s.bind((self.ip, self.port))


    def waitForUsers(self):
        self.waitUsers = True

        self.s.listen(5)

        # create thread to wait for new users
        self.waitEvent = Event()
        self.waitThread = Thread(target=self.__connectUsers)

        self.waitThread.start()

        return

    def __connectUsers(self):
        while(True):
            # listen to port to accept new users
            client_s, address = self.s.accept()

            print("User connected with address: "+str(address))

            # check to ensure new users still accepted
            thread = Thread(target=self.__signUserIn, args=(client_s, address))
            thread.start()
            
            time.sleep(0.1)

    def __signUserIn(self, client_s, address):
        # send client message asking for username
        client_s.send("Start||info||?".encode())

        # wait for message with the username
        info = str(client_s.recv(1024).decode()).split("||")

        if info[0] != "Info":
            print("Client gave invalid sign in packet")
            client_s.send("Error||Invalid sign in packet".encode())
            client_s.close()
            return

        if len(info) != 6:
            print("Client has outdated security key format")
            client_s.send("Error: Invalid security key, ensure client is up to date".encode())
            client_s.close()
            return
        
        cleared = self.authServer.userCleared(info[4])
        count = 0
        while(not cleared):
            print("User not cleared: "+str(address))
            if count > 10:
                print("User never cleared, removing.")
                client_s.send("Error||Invalid security key, ensure client is up to date".encode())
                client_s.close()
                return
            
            time.sleep(0.5)
            cleared = self.authServer.userCleared(info[4])
            count += 1


        print("Sign in info: "+str(info))

        username = info[1]
        code = int(info[2])
        create_account = info[3]

        # create new client for the array
        new_client = Client(username, address, client_s)

        # check to see if a user with this name exists
        if not new_client.userAccountExists() and create_account == "sign in":
            new_client.sendMessage("Error: User with name \'"+username+"\' does not exist")
            client_s.close()
            return
        # check to make sure account will not be overwritten
        if new_client.userAccountExists() and create_account == "create account":
            new_client.sendMessage("Error: User with name \'"+username+"\' already exists")
            client_s.close()
            return

        if create_account == "sign in":
            result = new_client.signInAccount(code)
        elif create_account == "create account":
            # ensure allowing a new account is allowed
            if not self.settings.allowNewUsers:
                new_client.sendMessage("Error: Creating new accounts is disabled")
                client_s.close()
                return

            result = new_client.createUserAccount(code)
        else:
            new_client.sendMessage("Error||invalid account sign in code")
            client_s.close()
            return
        
        # determine if sign in successful
        if not result:
            new_client.sendMessage("Error||Incorrect Username or Password")
            client_s.close()
            return

        if not self.waitUsers:
            new_client.sendMessage("Start||wait")
            self.waitingUsers += 1
            while(True):
                time.sleep(1)
                if self.waitUsers:
                    # add the new client to the array
                    self.clients.append(new_client)
                    self.waitingUsers -= 1
                    break
        else:
            # add the new client to the array
            self.clients.append(new_client)


        # send message to client stating complete
        new_client.sendMessage("Start||complete")
            
            

    def stopWaitingForUsers(self):
        self.waitUsers = False

    def startWaitingForUsers(self):
        self.waitUsers = True

    def getReadyFromUsers(self):
        curNumUsers = 0
        userResponses = []
        threads = []

        # enter an infintie loop
        while True:
            # determine if the number of users has changed
            if curNumUsers != len(self.clients):
                print("Detected New Users")
                # enter for loop to get all new added users
                i = curNumUsers
                for i in range(curNumUsers, len(self.clients)):
                    # append a blank element to the responses array
                    userResponses.append("--")
                    threads.append(Thread())

                    print(self.clients[i].toString())

                    # create a new thread to ask the user the ready question
                    threads[i] = Thread(target=self.clients[i].askQuestion, args = ("Start||ready||?", userResponses, i, 60))
                    threads[i].start()

                curNumUsers = len(self.clients)

            # determine if all users have said ready
            allReady = True
            for response in userResponses:
                if response[0:2] == "--":
                    allReady = False

            if not allReady:
                print("Still waiting...")
            else:
                # iterate over all elements, ensure each user has said yes
                i = 0
                for response in userResponses:
                    print(userResponses)
                    if response != "y":
                        print(self.clients[i].name+" was not ready")
                        try:
                            self.clients[i].sendMessage("quit")
                            self.clients[i].close()
                        except Exception as e:
                            print("Coult not send quit to: "+self.clients[i].name)
                        self.clients.pop(i)
                    i += 1

                print("All users ready!")
                break

            time.sleep(1)

    def sendMessageToAllUsers(self, msg: str):
        for client in self.clients:
            try:
                client.sendMessage(msg)
            except Exception as e:
                print(str(e)+"\n(Surpressed)")

    def sendMessageToAllExcept(self, msg: str, usr: str):
        for client in self.clients:
            if client.name != usr:
                try:
                    client.sendMessage(msg)
                except Exception as e:
                    print(str(e)+"\n(Surpressed)")

    def sendMessageToUser(self, name: str, msg: str) -> bool:
        client = self.getClientFromName(name)

        try:
            client.sendMessage(msg)
        except Exception as e:
            print("Detected dropped client by exception: "+name)
            self.clients.remove(client)
            return False
        
        return True

    def askQuestionToUser(self, name: str, msg: str) -> str:
        client = self.getClientFromName(name)

        try:
            response = client.askQuestion(msg)
        except Exception as e:
            print("Detected dropped client by exception: "+name)
            self.clients.remove(client)
            return None
        
        # catch if empty string was sent
        if response == "":
            print("Detected dropped client: "+name)
            self.clients.remove(client)
            return None

        return response



    def getClientFromName(self, name: str) -> Client:
        for client in self.clients:
            if client.name == name:
                return client
            
        raise Exception("No User: No user with this name was found")




        
                


        
