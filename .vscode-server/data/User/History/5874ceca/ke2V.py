import random

DECKSIZE: int = 52
NUMDECKS: int = 1

# SUITES
SUITES: int = 4
SPADE: int = 0
CLUBS: int = 1
HEARTS: int = 2
DIAMONDS: int = 3

# RANKS
RANKS: int = 14
JACK: int = 11
QUEEN: int = 12
KING: int = 13
ACE: int = 14

# HAND RESULTS
GOOD: int = 0
BUST: int = 1
BLACKJACK: int = 2
CARD21: int = 3


class Card:
    suite: int = -1
    rank: int = -1

    def __init__(self, suite: int, rank: int):
        self.suite = suite
        self.rank = rank

    def suite2Text(self) -> str:
        if self.suite == 0:
            return "S"
        elif self.suite == 1:
            return "C"
        elif self.suite == 2:
            return "H"
        elif self.suite == 3:
            return "D"
        else:
            return "INVALID"

    def rank2Text(self) -> str:
        if self.rank <= 10:
            return str(self.rank)
        elif self.rank == 11:
            return "J"
        elif self.rank == 12:
            return "Q"
        elif self.rank == 13:
            return "K"
        elif self.rank == 14:
            return "A"
        else:
            return "INVALID"
        
    def toString(self) -> str:
        return self.rank2Text() + ":" + self.suite2Text()

class Deck:
    cards: [Card] # type: ignore

    def __init__(self):
        self.cards = []
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
    cards: [Card] # type: ignore
    bet: int
    total: int

    def __init__(self):
        self.cards = []
        self.total = []

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

        # if more than one card, calculate the total
        if len(self.cards) > 1:
            self.total = self.totalCards()

    def clearHand(self):
        self.cards = []

    def totalCards(self) -> [int]: # type: ignore
        if (len(self.cards) == 0):
            return [0]

        totals: [int] = [0] # type: ignore
        # iterate over all cards
        for card in self.cards:
            # determine if current card is an ace
            if card.rank == ACE:
                # determine if 11 is possible
                if totals[0] + 11 <= 21:
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
                        totals[1] += 10
                    else:
                        # remove second element
                        totals.pop()
                
            # all other cards are totaled
            else:
                totals[0] += card.rank

                # determine if there was an ace and new card can be added to second total
                if len(totals) > 1:
                    if totals[1] + card.rank <= 21:
                        totals[1] += card.rank
                    else:
                        # remove the second element
                        totals.pop()
        
        return totals
    
    def getResult(self, totals = [-1]) -> int:
        if totals[0] == -1:
            totals = self.totalCards()

        # determine if there was a blackjack
        if len(self.cards) == 2 and len(totals) > 1:
            if totals[1] == 21:
                return BLACKJACK

        # determine all other situations
        if totals[0] > 21:
            return BUST
        elif totals[0] == 21:
            return CARD21
        else:
            return GOOD
        
    def result2String(self, result: int = None) -> str:
        if (result == None): result = self.getResult() 

        if result == BUST:
            return "BUST"
        elif result == BLACKJACK:
            return "BLACKJACK"
        elif result == CARD21:
            return str(len(self.cards)) + " card 21"
        else:
            totals = self.totalCards()
            if len(totals) > 1:
                return str(totals[0])+"|"+str(totals[1])
            
            return str(totals[0])

            
                


