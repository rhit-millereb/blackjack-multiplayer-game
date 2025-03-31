import tkinter as tk
from cards import *


if __name__ == "__main__":
    table: Table = Table()
    table.createStack()
    table.addUser("User 1")
    table.addUser("User 2")
    table.drawHands()
    print(table.toString(True))
