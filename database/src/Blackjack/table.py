from user import *
from server import *

class Stack:
    cards: [Card] # type: ignore

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
        if decks < -1: raise Exception("Invalid Deck Number: Num of decks must be greater than zero")
        if decks == -1: print("Warning: Making rigged deck!")

        print("Creating stack with: "+str(decks)+" decks")

        # if rigged, fill with only 10s
        if decks == -1:
            for i in range(50):
                self.cards += [Card(0, 10)]

            return

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

    def length(self) -> int:
        return len(self.cards)
        
        


class Table:
    stack: Stack
    dealer: Hand
    users: [User] # type: ignore
    settings: Settings

    def __init__(self, settings: Settings):
        self.dealer = Hand()
        self.users = []

        self.settings = settings

    def toString(self, showDealer: bool) -> str:
        text = "Table||"
        text += "Dealer:"+self.dealer.toString(showDealer)+"||"

        for user in self.users:
            text += user.data.name+":"
            for hand in user.hands:
                text += hand.toString(True)+":"+str(hand.bet)+":"+hand.result2String()+"||"

        return text

    def createStack(self):
        self.stack = Stack()
        if not self.settings.riggedShuffle:
            self.stack.create(NUMDECKS)
        else:
            self.stack.create(-1)

    def addUser(self, user: User):
        # give the user a blank hand
        user.addHand(Hand())
        # add user to array of users
        self.users.append(user)

    def drawHands(self, server: Server):
        # determine if cards can be drawn
        if not self.stack.canDraw(6+(6*len(self.users))):
            # not enough cards left, reshuffle
            print("\nSTACK OUT: RESHUFFLING\n")
            server.sendMessageToAllUsers("Message||Stack Out: Running shuffle algorithm...")
            time.sleep(3)
            self.stack.clear()
            self.stack.create(NUMDECKS)

        server.sendMessageToAllUsers("Deck||"+str(self.stack.length()))

        # draw the dealers hand
        for i in range(2):
            self.dealer.addCard(self.stack.drawCard())

        # draw the user's hands
        for user in self.users:
            for hand in user.hands:
                for i in range(2):
                    hand.addCard(self.stack.drawCard())

        server.sendMessageToAllUsers("Deck||"+str(self.stack.length()))


    # returns true if hand can make another move
    def userMove(self, user: User, hand: Hand, move: str, server: Server) -> bool:
        if (move == "hit" or move == "double"):
            # if double, double the bet
            if (move == "double"):
                # check if double is possible
                if (len(hand.cards) > 2):
                    print("Move not allowed")
                    server.sendMessageToUser(user.data.name, "Message||Move not allowed")
                    time.sleep(1)
                    return True
    
                # check if the bank allows for doubling
                if user.data.bank - hand.bet < 0:
                    print("Not enough bank")
                    server.sendMessageToUser(user.data.name, "Message||Move not allowed, broke bitch")
                    time.sleep(1)
                    return True

                user.data.bank -= hand.bet
                hand.bet += hand.bet

                server.sendMessageToAllExcept("Message||"+user.data.name+" DOUBLES DOWN", user.data.name)

                user.updateToFile()

            # add a card to the user
            self.hitUser(hand)

            server.sendMessageToAllUsers("Deck||"+str(self.stack.length()))
            
            print(user.data.name+": "+hand.toString(True))
            print(user.data.name+" now has: "+hand.result2String())
            
            server.sendMessageToAllUsers("Update||"+user.data.name+":"+user.hand2String())


            # determine if the hand busts
            if (hand.total[0] > 21):
                hand.clearHand()
                hand.total = [0]
                hand.bet = 0
                return False
            elif hand.total[0] == 21: return False
            elif move == "double": return False

            return True
        elif (move == "stand"):
            server.sendMessageToAllUsers("Message||"+user.data.name+" stands")

            return False
        elif (move == "split"):
            # ensure that the hand only has two cards, and both are equal
            if not hand.splitable():
                print("Split not allowed")
                server.sendMessageToUser(user.data.name, "Message||Split not allowed")
                time.sleep(1)
                return True

            # determine if the bank has enough
            if user.data.bank - hand.bet < 0:
                print("Split not allowed, money")
                server.sendMessageToUser(user.data.name, "Message||Split not allowed, broke bitch")
                time.sleep(1)
                return True

            # create a second hand and add the second card from original hand
            secondCard = hand.cards.pop()
            newHand = Hand()
            newHand.addCard(secondCard)
            newHand.bet = hand.bet
            # hit the second hand with another card
            self.hitUser(newHand)
            # add the hand to the user
            user.addHand(newHand)

            # hit the original hand with another card
            self.hitUser(hand)

            # remove bet from bank
            user.data.bank -= hand.bet

            print("Hand Split.")
            print("Original Hand now: "+hand.toString(True)+" ("+hand.result2String()+")")
            print("Second Hand is: "+newHand.toString(True)+" ("+newHand.result2String()+")")

            server.sendMessageToAllUsers("Message||"+user.data.name+" split hand.")
            server.sendMessageToAllUsers("Update||"+user.data.name+":"+user.hand2String())
            server.sendMessageToAllUsers("Deck||"+str(self.stack.length()))
            time.sleep(1)

            return True
        else:
            print("Invalid move")
            server.sendMessageToUser(user.data.name, "Message||Invalid move")
            time.sleep(1)
            return True

    def hitUser(self, hand: Hand):
        hand.addCard(self.stack.drawCard())

    def doesDealerHit(self) -> bool:
        total = self.dealer.totalCards()

        # if dealer has an ace
        if (len(total) > 1):
            # dealer has ace, hit on soft 17
            if (total[1] <= 17):
                return True
            return False
        else:
            # dealer has no ace, hit when over 16
            if (total[0] < 17):
                return True
            return False

    def hitDealer(self) -> Card:
        card = self.stack.drawCard()
        self.dealer.addCard(card)

        return card

    def clearTable(self):
        self.dealer.clearHand()

        for user in self.users:
            user.hands = [Hand()]

    def getUserFromName(self, name: str) -> User:
        for user in self.users:
            if user.data.name == name:
                return user
            
        return None
