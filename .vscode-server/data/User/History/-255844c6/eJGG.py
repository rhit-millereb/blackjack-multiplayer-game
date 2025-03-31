import time
from cards import *

SETUP: int = 0
DEALING: int = 1
BETS: int = 2
GAME: int = 3

HIT: int = 0
STAND: int = 1
SPLIT: int = 2
DOUBLE: int = 3

class Game:

    state: int
    table: Table

    dealerTotal: int
    userTotals: [int]
    userChoise: [int]

    def __init__(self):
        self.state = SETUP

        self.dealerTotal = 0
        self.userTotals = []
        self.userChoise = []

    # called when the table is set up and assigned here
    def assignTable(self, table: Table):
        self.table = table

        # add appropriate num of elements to user arrays
        for i in range(len(self.table.users)):
            self.userTotals.append(-1)
            self.userChoise.append(-1)

    def begin(self):
        if self.state != SETUP:
            raise Exception("Cannot Start: Game must be in setup state to start a new game")
        
        self.state = DEALING
        self.gameLoop()
        
    def gameLoop(self):
        # enter an infinite loop
        while(True):
            if self.state == SETUP:
                # stop the loop
                return
            elif self.state == DEALING:
                # create the stack
                self.table.createStack()
                # draw the hands
                self.table.drawHands()
                # show all of the cards
                print(self.table.toString(False))
                # set state to bets
                self.state = BETS
            elif self.state == BETS:
                pass
            elif self.state == GAME:
                pass

            time.sleep(0.1)
        

        
