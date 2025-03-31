import tkinter as tk
from game import *


if __name__ == "__main__":
    # create an instance of the settings object
    settings = Settings()

    # create an instance of the server, and make it wait for users
    server = Server(settings)
    print("Server started.")
    server.waitForUsers()

    # enter an infinite loop so the server always waits when user queue is empty
    while(True):
        settings.parseSettingsFile()
        print("Waiting for users...")
        # wait until the server has at least one client connected
        while(True):
            time.sleep(1)
            if len(server.clients) > 0:
                print("Server has connections")
                break

        try:
            server.getReadyFromUsers()
        except Exception as e:
            print("/////////////////Error waiting for users to join////////////////\n"+str(e))
            continue

        print("Game ready to begin")
        server.sendMessageToAllUsers("Message||Game ready! Waiting for users to place bets...")

        # stop new users from joining
        server.stopWaitingForUsers()

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
        try:
            game.begin()
        except Exception as e:
            print("///////////////Exception During Game////////////////\n\t"+str(e)+"\n")
            print(e)
            server.sendMessageToAllUsers("Error||During game:\n"+str(e))

        print("Game ended, returning to wait...")
        # reallow users to join
        server.startWaitingForUsers()
