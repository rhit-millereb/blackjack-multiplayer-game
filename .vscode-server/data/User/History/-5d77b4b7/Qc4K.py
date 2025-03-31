import socket
import threading

CHAT_PORT = 3070

class Chat:
    clientIDs: [str] # type: ignore

    joinThread: threading.Thread
    chatThread: threading.Thread

    def __init__(self, clientIDs):
        self.clientIDs = clientIDs

        self.s = socket.socket()
        self.s.bind(("192.168.0.181", CHAT_PORT))

    def start(self):
        self.s.listen(10)

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
            client_s.close()
            return
        
        clientID = rsp[1]

        



    def print(self, msg):
        print("Chat: "+str(msg))



