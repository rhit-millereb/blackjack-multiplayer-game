import tkinter as tk
from game import *


if __name__ == "__main__":
    # create an instance of the server, and make it wait for users
    server = Server()
    server.waitForUsers()

    # wait until the server has at least one client connected
    while(True):
        time.sleep(1)
        if len(server.clients) > 0:
            print("Server has connections")
            break

    server.getReadyFromUsers()

    print("Game ready to begin")
    server.sendMessageToAllUsers("Game ready! Starting...")

    # create an instance of the table
    table = Table()
    # iterate over each client, and create a user
    for client in server.clients:
        # create a new user instance
        user = User()
        user.signUserIn(client.name, client.code)

        # add user to table
        table.addUser(user)



    # create the table
#    table: Table = Table()
    
    # what for users to join
#    print("Enter user names:")


#    while(True):
#        username = input("Username: ")

#        if username == "start":
#            break
#        else:
#            code = int(input("Code: "))

#            try:
#                user = User(username, code)
#            except Exception as e:
#                print(str(e))
#                continue

#            table.addUser(user)


#    game: Game = Game()
#    game.assignTable(table)

#    game.begin()