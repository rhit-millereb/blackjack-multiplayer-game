import time
from table import *
from settings import Settings


HIT: int = 0
STAND: int = 1
SPLIT: int = 2
DOUBLE: int = 3

class Game:

    table: Table

    server: Server

    dealerTotal: int

    def __init__(self):
        self.dealerTotal = []

    # called when the table is set up and assigned here
    def assignTable(self, table: Table):
        self.table = table

    # called when the server is set up and assigned
    def assignServer(self, server: Server):
        self.server = server

    def begin(self):
        if self.server is None:
            raise Exception("Cannot Start: Server must be assigned")
        if self.table is None:
            raise Exception("Cannot State: Table must be assigned")

        # create the stack
        self.table.createStack()

        self.gameLoop() # nothing below this line will run
        
    def gameLoop(self):
        # enter an infinite loop
        while(True):
            # create an array of users to remove
            usersToRemove = []

            # iterate to each user and collect bets
            for user in self.table.users:
                # send message to user, if fails remove user from array
                if not self.server.sendMessageToUser(user.data.name, "Bank||"+str(user.data.bank)):
                    usersToRemove.append(user)
                    continue

                print(str(user.data.bank)+" credits available")
                
                time.sleep(1)

                # detect if the user has no money, skip them and remove from users
                if (user.data.bank <= 0):
                    self.server.sendMessageToUser(user.data.name, "Message||You're a broke bitch, removing from game...")
                    print(user.data.name+" is broke, removing from game...")
                    self.server.sendMessageToUser(user.data.name, "quit")
                    usersToRemove.append(user)
                    continue

                # iterate over all the hands of the user to add bets for
                i = 0
                for hand in user.hands:
                    # send message to all other users
                    self.server.sendMessageToAllExcept("Message||Waiting for bet from: "+user.data.name, user.data.name)
                    # ask the user for their bet, if None, remove the user
                    bet = self.server.askQuestionToUser(user.data.name, "Game||bet||"+str(i+1)+"||?")
                    if bet is None or bet == "":
                        self.server.sendMessageToUser("Message||Leaving game...")
                        usersToRemove.append(user)
                        break

                    try:
                        bet = int(bet)
                    except Exception as e:
                        usersToRemove.append(user)
                        return

                    if bet <= 0:
                        self.server.sendMessageToUser(user.data.name, "Error||Fuck off")
                        usersToRemove.append(user)
                        break

                    if bet >= user.data.bank:
                        self.server.sendMessageToUser(user.data.name, "Error||Gotcha Fat Ass")
                        usersToRemove.append(user)
                        break

                    user.data.bank -= bet
                    user.updateToFile()

                    hand.bet = bet

                    i += 1

            # iterate over each users that was flagged to remove, and remove them
            for user in usersToRemove:
                print("Removing: "+user.data.name)
                self.table.users.remove(user)

            # if num of users is zero, return, ending the game
            if (len(self.table.users) == 0): 
                return

            self.server.sendMessageToAllUsers("Message||Bets are now closed")
            time.sleep(1)

            # ///////////////////////////////////////////// DEALING ///////////////////////////////////////////////
                
            # draw the hands
            self.table.drawHands(self.server)
            # show all of the cards
            print("\n"+self.table.toString(False))
            # send message to all users
            try:
                self.server.sendMessageToAllUsers(self.table.toString(False))
            except Exception as e:
                print(str(e)+"(Surpressed)")


            # total all of the dealers cards
            self.dealerTotal = self.table.dealer.totalCards()
            if (self.table.dealer.getResult(self.dealerTotal) == BLACKJACK):
                time.sleep(2)

                self.server.sendMessageToAllUsers(self.table.toString(True))
                print("Dealer has blackjack")

                # send the blackjack message to all users
                try:
                    self.server.sendMessageToAllUsers("Message||DEALER HAS BLACKJACK")
                except Exception as e:
                    print(str(e)+"\n(Surpressed)")

                time.sleep(2)

                self.reset()
                continue

            # ////////////////////////////////////////// GAME /////////////////////////////////////////////////

            usersToRemove = []

            # iterate to each user and ask for move
            for user in self.table.users:
                i = 0
                for hand in user.hands:
                    # catch if the hand already has blackjack
                    if (len(hand.total) > 1):
                        if (hand.total[1] == 21):
                            hand.bet += int((3/2)*hand.bet)
                            continue
                    
                    # ask user for move
                    move = self.server.askQuestionToUser(user.data.name, "Game||move||"+str(i+1)+"||?")
                    # if move was none, remove the user
                    if move is None:
                        # user connection error, remove user and break loop
                        usersToRemove.append(user)
                        break
                    
                    # keep asking for moves while possible
                    timeout = False
                    while(self.table.userMove(user, hand, move, self.server)):
                        move = self.server.askQuestionToUser(user.data.name, "Game||move||"+str(i+1)+"||?")
                        if move is None:
                            # user connection error, remove user and break loop
                            timeout = True
                            usersToRemove.append(user)
                            break
                    
                    if timeout:
                        break

                    i+=1

            # remove users that were flagged
            for user in usersToRemove:
                self.table.users.remove(user)

            # /////////////////////////////////////////////// DEALER ///////////////////////////////////////////////////

            # reveal the dealers cards
            print("Dealer:"+self.table.dealer.toString(True)+"("+self.table.dealer.result2String()+")")
            
            self.server.sendMessageToAllUsers("Update||Dealer:"+self.table.dealer.toString(True)+":"+self.table.dealer.result2String()+"")

            while (self.table.doesDealerHit()):
                time.sleep(1)
                # get the card the dealer pulled and their result
                card = self.table.hitDealer()
                result = self.table.dealer.getResult()

                print("Dealer Hits, Pulled: "+card.toString()+" ("+self.table.dealer.result2String()+")")

                try:
                    self.server.sendMessageToAllUsers("Update||Dealer:"+self.table.dealer.toString(True)+":"+self.table.dealer.result2String())
                    self.server.sendMessageToAllUsers("Message||Dealer Hits ("+self.table.dealer.result2String()+")")
                    self.server.sendMessageToAllUsers("Deck||"+str(self.table.stack.length()))
                    time.sleep(1)
                except Exception as e:
                    print(str(e)+"\n(Surpressed)")

                if (result == BUST):
                    self.dealerTotal = []
                    self.table.dealer.clearHand()
                    break

            # get new dealer total
            dealerTotal = self.table.dealer.totalCards()
            # if had an ace, choose greater results
            if len(dealerTotal) > 1:
                dealerTotal = dealerTotal[1]
            else:
                dealerTotal = dealerTotal[0]

            # //////////////////////////////////////////////// RESULTS ////////////////////////////////////////////////////

            usersToRemove = []
            # determine which players won
            for user in self.table.users:
                i = 0
                text = "Message||"
                for hand in user.hands:
                    # determine if an ace is in the user hand
                    if len(hand.total) > 1:
                        total = hand.total[1]
                    else:
                        total = hand.total[0]

                    if (total < dealerTotal or total == 0):
                        print(user.data.name+" hand "+str(i+1)+" looses")

                        text += "Hand "+str(i+1)+" looses~"

                        user.data.losses += 1
                    elif (total == dealerTotal):
                        print(user.data.name+" hand "+str(i+1)+" push")
                        
                        text += "Hand "+str(i+1)+" push~"

                        # add the bet hand back to the user
                        user.data.bank += hand.bet
                    else:
                        print(user.data.name+" hand "+str(i+1)+" wins")
                        
                        text += "Hand "+str(i+1)+" wins!~"

                        user.data.wins += 1

                        # check if hand had blackjack, if so, bet has already been increased
                        if not (total == 21 and len(hand.cards) == 2):
                            # add bets to user bank
                            user.data.bank += 2 * hand.bet
                        else:
                            user.data.bank += hand.bet

                    i += 1
                
                # send the message to the client
                if not self.server.sendMessageToUser(user.data.name, text[:-1]):
                    # append user to users to remove and break from hands loop
                    usersToRemove.append(user)
                    break

                # update user bank to file
                user.updateToFile()
            
            # remove all users that were flagged
            for user in usersToRemove:
                self.table.users.remove(user)

            # reset all user hands
            self.reset()

            time.sleep(2)

            # determine if any clients are waiting
            if self.server.waitingUsers > 0:
                self.server.startWaitingForUsers()

                # wait for threads to add all users
                if self.server.waitingUsers > 0:
                    self.server.sendMessageToAllUsers("Message||Adding new users to game...")
                while(self.server.waitingUsers > 0):
                    time.sleep(0.1)

                # iterate over all clients, detect if client is not a signed in user
                for client in self.server.clients:
                    if self.table.getUserFromName(client.name) is None:
                        user = User()
                        user.signUserIn(client.name, client.code)

                        self.table.addUser(user)

                        print("Added user \'"+client.name+"\' to the active game")
                        self.server.sendMessageToAllExcept("Message||Added "+client.name+" to the game!", client.name)
                        time.sleep(1)

                # disable more users from joining
                self.server.stopWaitingForUsers()
        

    def reset(self):
        self.table.clearTable()
        
