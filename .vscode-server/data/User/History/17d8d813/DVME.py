import tkinter as tk
from game import *


if __name__ == "__main__":
    # create the table
    table: Table = Table()
    
    # what for users to join
    while(True):
        response = input()

        if response == "start":
            break
        else:
            table.addUser(response)

    game: Game = Game()