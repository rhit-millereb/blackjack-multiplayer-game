from cards import *

SETUP: int = 0
BETS: int = 1
DEALING: int = 2
GAME: int = 3

class Game:

    state: int
    table: Table

    dealerTotal: int
    userTotals: [int]

    def __init__(self):
        self.state = SETUP

        self.dealerTotal = 0
        self.userTotals = []

    # called when the table is set up and assigned here
    def assignTable(self, table: Table):
        self.table = table

        for i in range(len(self.table.users)):
            self.userTotals.append(0)

    def begin(self):
        if self.state != SETUP:
            raise Exception("Cannot Start: Game must be in setup state to start a new game")
        

        
