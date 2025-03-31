import tkinter as tk
from game import *


if __name__ == "__main__":
    # create the table
    table: Table = Table()
    
    # what for users to join
    print("Enter user names:")

    for i in range(10):
        table.addUser("User "+str(i))

#    while(True):
#        response = input()

#        if response == "start":
#            break
#        else:
#            table.addUser(response)

    game: Game = Game()
    game.assignTable(table)

    game.begin()