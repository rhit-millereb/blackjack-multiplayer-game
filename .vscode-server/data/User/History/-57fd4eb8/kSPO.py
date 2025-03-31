import tkinter as tk
from game import *


if __name__ == "__main__":
    # create an instance of the server, and make it wait for users
    server = Server()
    server.waitForUsers()

    # enter an infinite loop so the server always waits when user queue is empty
    while(True):
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

        # create an instance of the game
        game = Game()
        # assign table/server to the game
        game.assignTable(table)
        game.assignServer(server)

        # start the game
        game.begin()

        print("Game ended, returning to wait...")