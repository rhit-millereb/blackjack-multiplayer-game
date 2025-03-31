from cards import *

SETUP: int = 0
BETS: int = 1
DEALING: int = 2
GAME: int = 3

class Game:

    state: int
    table: Table


    def __init__(self):
        self.state = SETUP

    # called when the table is set up and assigned here
    def assignTable(self, table: Table):
        self.table = table

    def begin():
        