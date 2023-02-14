#Unit Tests for hw1
#to run game: python3 driver.py
#to run unit tests: coverage run -m unittest discover 
#to test coverage: coverage run => then coverage report

from card import Card

class Dealer:
    def __init__(self, hand):
        self.hand = hand
    
    def stand(self):
        print("\nDealer total hand is >=17, he stands")
    
    def hit(self, card):
        print("\nDealer total hand is < 17, he hits")
        self.hand.append(card)
    
    def revealFirstCard(self):
        print("\nDealer's first card is: " + str(self.hand[0]))
    
    def revealEntireHand(self):
        print("\nDealer's hand is: " + str(self.hand))
    
    def payout(self, wage, wallet):
        print("\nCongratulations: you win: $" + str(wage) + " you now have $" + str(wage + wallet) + " in your wallet")

    def __repr__(self):
        return "\nDealer: hand:% s" % (self.hand)

    def clearHand(self):
        self.hand = []