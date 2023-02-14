#Unit Tests for hw1
#to run game: python3 driver.py
#to run unit tests: coverage run -m unittest discover 
#to test coverage: coverage run => then coverage report

from card import Card

class Player:
    def __init__(self, hand, wage, wallet):
        self.wallet = wallet
        self.hand = hand
        self.wage = wage
        self.hand2 = []
        self.wage2 = 0

    def hit(self, card):
        print("\nPlayer chooses to Hit")
        self.hand.append(card)
    
    def stand(self):
        print("\nPlayer chooses to Stand")
    
    def doubleDown(self, card): #double wage and hit once 
        print("\nPlayer chooses to Double Down")
        self.wage = self.wage * 2
        self.hand.append(card)
    
    def split(self, newWage, newCard1, newCard2): #if hand is equal value, you can add second wage and split into two hands, now you have two standing bets.
        print("\nPlayer chooses to Split")
        self.wage2 = newWage
        tmp = self.hand[1]
        self.hand = [self.hand[0], newCard1]
        self.hand2 = [tmp, newCard2]

    
    def surrender(self):
        print("\nPlayer Chooses to Surrender. You lost " + str(int(self.wage/2)))
        self.wallet = self.wallet - int((self.wage/2))
    
    def revealHand(self):
        print("\nPlayer's hand: ") 
        print(str(self.hand))
    
    def revealSplitHands(self):
        print("\nPlayer hands are: ")
        print("hand 1: " + str(self.hand))
        print("hand2: " + str(self.hand2))

    def loseWage(self, split=False):
        if split:
            self.wallet = self.wallet - self.wage2
            print("\nSorry, you lost: $" + str(self.wage2) + " your new wallet balance is: $" + str(self.wallet))
        else:
            self.wallet = self.wallet - self.wage
            print("\nSorry, you lost: $" + str(self.wage) + " your new wallet balance is: $" + str(self.wallet))

    def __repr__(self):
        return "Player: wallet:% s hand:% s, wage:% s, hand2:% s, wage2:% s" % (self.wallet, self.hand, self.wage, self.hand2, self.wage2)

    def clearHand(self):
        self.hand = []
        self.hand2 = []