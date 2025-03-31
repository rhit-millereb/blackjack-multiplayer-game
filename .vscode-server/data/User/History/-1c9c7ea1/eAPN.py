import array
import random

DECKSIZE: int = 52
NUMDECKS: int = 4

# SUITES
SUITES: int = 4
SPADE: int = 0
CLUBS: int = 1
HEARTS: int = 2
DIAMONDS: int = 3

# RANKS
RANKS: int = 13
JACK: int = 11
QUEEN: int = 12
KING: int = 13
ACE: int = 14

# HAND RESULTS
GOOD: int = 0
BUST: int = 1
BLACKJACK: int = 2


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
            for rank in range(2, RANKS+1):
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

    def toString(self, showAll: bool) -> str:
        all = ""
        if showAll:
            for card in self.cards:
                all += card.toString()+", "
            return all[:-2]
        else:
            return self.cards[0].toString()

    def addCard(self, card: Card):
        self.cards.append(card)

    def clearHand(self):
        self.cards = []

    def totalCards(self) -> [int]:
        totals: [int] = [0]
        # iterate over all cards
        for card in self.cards:
            # determine if current card is an ace
            if card.rank == ACE:
                # determine if 11 is possible
                if totals[0] + 11 <= 21 and len(totals) == 1:
                    # determine if there was already an ace
                    if len(totals) == 1:
                        totals.append(totals[0] + 11)
                    else:
                        # already was an ace, add one to the 11 total
                        totals[1] += 1
                
                totals[0] += 1

            # determine if a face card: rank will be > 10
            elif card.rank > 10:
                totals[0] += 10

                # determine if there was an ace and new card can be added to second total
                if len(totals) > 1:
                    if totals[1] + 10 <= 21:
                        totals[1] += 1
                
            # all other cards are totaled
            else:
                totals[0] += card.rank

                # determine if there was an ace and new card can be added to second total
                if len(totals) > 1:
                    if totals[1] + card.rank <= 21:
                        totals[1] += card.rank
        
        return totals
    
    def getResult(self, totals = [-1]) -> int:
        if totals[0] == -1:
            totals = self.totalCards()

        if totals[0] > 21:
            return BUST
        elif totals[0] == 21:
            return BLACKJACK
        else:
            return GOOD
        
    def result2String(self, result: int) -> str:
        if result == BUST:
            return "BUST"
        elif result == BLACKJACK:
            return "BLACKJACK"
        else:
            totals = self.totalCards()
            if len(totals) > 1:
                return str(totals[0])+"|"+str(totals[1])
            
            return str(totals[0])
                



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
            print(len(deck))
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
            text += self.users[i].name+": "+self.users[i].toString(True)+"\n"

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

