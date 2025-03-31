import time
from cards import *

SETUP: int = 0
BETS: int = 1
DEALING: int = 2
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
    userBets: [int]

    def __init__(self):
        self.state = SETUP

        self.dealerTotal = 0
        self.userTotals = []
        self.userChoise = []
        self.userBets = []

    # called when the table is set up and assigned here
    def assignTable(self, table: Table):
        self.table = table

        # add appropriate num of elements to user arrays
        for i in range(len(self.table.users)):
            self.userTotals.append(-1)
            self.userChoise.append(-1)
            self.userBets.append(-1)

    def begin(self):
        if self.state != SETUP:
            raise Exception("Cannot Start: Game must be in setup state to start a new game")
        
        # create the stack
        self.table.createStack()

        # set the state to bet setting and start the game loop
        self.state = BETS
        self.gameLoop() # nothing below this line will run
        
    def gameLoop(self):
        # enter an infinite loop
        while(True):
            if self.state == SETUP:
                # stop the loop
                return
            elif self.state == BETS:
                # iterate to each user and collect bets
                for user in self.table.users:
                    
            elif self.state == DEALING:
                
                # draw the hands
                self.table.drawHands()
                # show all of the cards
                print(self.table.toString(False))

                # total all of the dealers cards

                # total all of the user's cards

                # set the state to the game
                self.state = GAME
            elif self.state == GAME:
                pass

            time.sleep(0.1)
        

        
