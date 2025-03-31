import socket
import threading
from server import *

CHAT_PORT = 3070

class Chat:
    clientIDs: [str] # type: ignore

    # reference to main client connections to get usernmae
    clients: [] # type: ignore

    # list of all current chat connections
    connections: []

    joinThread: threading.Thread
    chatThread: threading.Thread

    def __init__(self, clientIDs, clients):
        self.clientIDs = clientIDs
        self.clients = clients

        self.connections = []

        self.print("Starting...")

        self.s = socket.socket()
        self.s.bind(("192.168.0.181", CHAT_PORT))

        self.start()

    def start(self):
        self.s.listen(5)

        self.chatThread = threading.Thread(target=self.join_users)
        self.chatThread.start()

    def join_users(self):
        while True:
            # listen for new users
            client, address = self.s.accept()

            self.print("Connected with "+str(address))

            thread = threading.Thread(target=self.userSendsMessage, args=(client, ))
            thread.start()

    def userSendsMessage(self, client_s: socket.socket):
        # send connected message
        client_s.send("Chat||connected".encode())
        
        # check received message
        rsp = client_s.recv(1024).decode().split("||")
        print(rsp)
        if rsp[0] != "Chat":
            self.print("User sent invalid response")
            client_s.send("Error||Invalid response")
            client_s.close()
            return
        
        clientID = rsp[1]

        try:
            username = self.get_username_from_client(clientID)
        except Exception as e:
            self.print("No user with matching ID")
            client_s.close("Error||No user with matching client ID")
            client_s.close()
            return
        
        self.print("User connected with: "+username)
        client_s.send("Chat||confirmed")

        self.connections.append(client_s)

        while True:
            # encase in try catch to catch when user disconnects
            try:
                msg = client_s.recv(1024).decode().split("||")
            except Exception as e:
                self.print(username+" chat error, removing...")
                self.connections.remove(client_s)
                client_s.close()
                return
            
            if len(msg) != 3:
                    client_s.send("Error||Invalid message packet")
                    continue

            if msg[1] != clientID:
                client_s.send("Error||User had tried to change username")
                continue

            if len(msg[2]) > 150:
                client_s.send("Error||Message too long, max 150 characters")
                continue

            connectionsToRemove = []
            for connection in self.connections:
                try:
                    connection.send("Message||"+username+"||"+msg[2])
                except Exception as e:
                    connection.close()
                    connectionsToRemove.append(connection)

            for connection in connectionsToRemove:
                self.connections.remove(connection)

        
    def get_username_from_client(self, id) -> str:
        for client in self.clients:
            if client.clientID == id:
                return client.name
            
        raise Exception("No client found with matching client ID")


    def print(self, msg):
        print("Chat: "+str(msg))



