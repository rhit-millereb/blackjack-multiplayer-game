import array
import random

DECKSIZE: int = 52
NUMDECKS: int = 4

SUITES: int = 4
SPADE: int = 0
CLUBS: int = 1
HEARTS: int = 2
DIAMONDS: int = 3

RANKS: int = 14
JACK: int = 11
QUEEN: int = 12
KING: int = 13
ACE: int = 14

class Card:
    suite: int = -1
    rank: int = -1

    def __init__(self, suite: int, rank: int):
        self.suite = suite
        self.rank = rank

    def suite2Text(self) -> str:
        if self.suite == 0:
            return "Spades"
        elif self.suite == 1:
            return "Clubs"
        elif self.suite == 2:
            return "Hearts"
        elif self.suite == 3:
            return "Diamonds"
        else:
            return "INVALID"

    def rank2Text(self) -> str:
        if self.rank <= 10:
            return str(self.rank)
        elif self.rank == 11:
            return "Jack"
        elif self.rank == 12:
            return "Queen"
        elif self.rank == 13:
            return "King"
        elif self.rank == 14:
            return "Ace"
        else:
            return "INVALID"
        
    def toString(self) -> str:
        return self.rank2Text() + " of " + self.suite2Text()

class Deck:
    cards: [Card] = []

    def __init__(self):
        pass

    def deck2String(self):
        all: str = ""
        for card in self.cards:
            all += card.toString()+"\n"
    
        return all


    def buildDeck(self):
        for suite in range(SUITES):
            for rank in range(1, RANKS+1):
                self.cards.append(Card(suite, rank))
    
    def shuffleDeck(self):
        random.shuffle(self.cards)

    def clearDeck(self):
        self.cards = []




class Hand:
    cards: [Card]
    name: str

    def __init__(self, name: str):
        self.cards = []
        self.name = name

    def toString(self) -> str:
        all = ""
        for card in self.cards:
            all += card.toString()+", "
        return all[:-2]

    def addCard(self, card: Card):
        self.cards.append(card)

    def clearHand(self):
        self.cards = []


class Stack:
    cards: [Card]

    def __init__(self):
        self.cards = []
        pass

    def toString(self) -> str:
        all: str = ""
        for card in self.cards:
            all += card.toString()+"\n"
    
        return all

    def create(self, decks: int):
        if decks is None: raise Exception("Invalid Deck Number: Must prove number of decks to use")
        if decks <= 0: raise Exception("Invalid Deck Number: Num of decks must be greater than zero")

        # add in cards according to the number of decks
        for i in range(decks):
            deck = Deck()
            deck.buildDeck()
            deck.shuffleDeck()

            self.cards += deck.cards

        # shuffle all the decks together
        random.shuffle(self.cards)
    
    def clear(self):
        self.cards = []

    # must include number of cards to be drawn
    def canDraw(self, num: int):
        return not (len(self.cards)-num < 0)

    def drawCard(self) -> Card:
        if not self.canDraw(1): raise Exception("Cannot Draw: No cards in stack")

        return self.cards.pop()
        
        


class Table:
    stack: Stack
    dealer: Hand
    users: [Hand]

    def __init__(self):
        self.dealer = Hand("dealer")
        self.users = []

    def toString(self, showDealer: bool) -> str:
        text = "Table:\n"
        text += self.dealer.name+": "+self.dealer.toString(showDealer)+"\n"

        for i in range(len(self.users)):
            text += self.users[i].name+": "+self.users[i].toString()+"\n"

        return text

    def createStack(self):
        self.stack = Stack()
        self.stack.create(NUMDECKS)

    def addUser(self, name: str):
        self.users.append(Hand(name))

    def drawHands(self):
        # determine if cards can be drawn
        if not self.stack.canDraw(2+(2*len(self.users))):
            # not enough cards left, reshuffle
            self.stack.clear()
            self.stack.create(NUMDECKS)

        # draw the dealers hand
        for i in range(2):
            self.dealer.addCard(self.stack.drawCard())

        # draw the user's hands
        for user in self.users:
            for i in range(2):
                user.addCard(self.stack.drawCard())

