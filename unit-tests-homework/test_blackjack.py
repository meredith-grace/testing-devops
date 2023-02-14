#Unit Tests for hw1
#to run game: python3 driver.py
#to run unit tests: coverage run -m unittest discover 
#to test coverage: coverage run => then coverage report

from driver import *
from card import Card

import unittest

pcard1 = Card("hearts", "A", 11)
pcard2 = Card("diamonds", "K", 10)
pwage = 4
pwallet = 50

dcard1 = Card("hearts", "Q", 10)
dcard2 = Card("diamonds", "9", 9)

player1 = Player([pcard1, pcard2], pwage, pwallet)
dealer1 = Dealer([dcard1, dcard2])

dealer2 = Dealer([dcard1, dcard2])
dealer3 = Dealer([dcard1, dcard2])

player2 = Player([pcard1, pcard2], pwage, pwallet)
player3 = Player([pcard1, pcard2], pwage, pwallet)

splitCard1 = Card("hearts", "3", 3)
splitCard2 = Card("diamonds","3", 3)
player4 = Player([splitCard1, splitCard2], pwage, pwallet)
player5 = Player([splitCard1, splitCard2], pwage, pwallet)


class TestBlackJack(unittest.TestCase):
	#driver.py
	def test_wentbroke(self):
		self.assertTrue(wentBroke(-1))
		self.assertFalse(wentBroke(4))
	
	def test_canplayagain(self):
		self.assertTrue(canPlayAgain("yes"))
		self.assertTrue(canPlayAgain("y"))
		self.assertFalse(canPlayAgain("n"))
		self.assertFalse(canPlayAgain("o"))

	#game.py
	def test_sumhand(self):
		self.assertEqual(21, sumHand(player1.hand))
		self.assertEqual(19, sumHand(dealer1.hand))
	
	def test_checkace(self):
		self.assertEqual(13, checkAce(player1.hand, 23))
		self.assertEqual(21, checkAce(player1.hand, 21))
	
	def test_isfirstround(self):
		self.assertTrue(isFirstRound(None, None))
		self.assertFalse(isFirstRound(player1, dealer1))
	
	def test_validWage(self):
		self.assertTrue(validWage(4, 50))
		self.assertFalse(validWage(50, 4))
		self.assertFalse(validWage(0, 50))
	
	def test_dealersturn(self):
		self.assertEqual(19, dealersTurn(dealer1))
	
	def test_hasblackjack(self):
		self.assertTrue(hasBlackJack(21))
		self.assertFalse(hasBlackJack(13))
	
	def test_checkwinner(self):
		self.assertEqual("dealer", checkWinner(20, 19))
		self.assertEqual("dealer", checkWinner(19, 23))
		self.assertEqual("player", checkWinner(18, 20))
		self.assertEqual("player", checkWinner(24, 15))

	def test_dealcards(self):
		d = Deck()
		wg = 4
		wll = 30
		dlr = Dealer([d.deck[0], d.deck[1]])
		plr = Player([d.deck[2], d.deck[3]], wg, wll)

		dlrT, plrT = dealCards(d, wg, wll)

		self.assertEqual(dlr.hand, dlrT.hand)
		self.assertEqual(plr.hand, plrT.hand)
		self.assertEqual(plr.wage, plrT.wage)
		self.assertEqual(plr.wallet, plrT.wallet)
	
	#deck.py
	def test_draw(self):
		d = Deck()
		self.assertEqual(d.deck[0], d.draw())
	
	def test_shuffle(self):
		d = Deck()
		d.draw()
		d.draw()
		d.shuffle()

		self.assertEqual(-1, d.index)
	
	#player.py
	def test_playerhit(self):
		newCard = Card("hearts", "2", 2)
		newHand = [pcard1, pcard2, newCard]
		player2.hit(newCard)

		self.assertEqual(newHand, player2.hand)
	
	def test_playerdoubledown(self):
		newCard = Card("hearts", "1", 1)
		newHand = [pcard1,pcard2,newCard]
		newWage = 8

		player3.doubleDown(newCard)

		self.assertEqual(newHand, player3.hand)
		self.assertEqual(newWage, player3.wage)
	
	def test_playersplit(self):
		newCard1 = Card("spades", "Q", 10)
		newCard2 = Card("spades", "K", 10)
		newWage = 8
		newHand1 = [splitCard1, newCard1]
		newHand2 = [splitCard2, newCard2]

		player4.split(newWage, newCard1, newCard2)

		self.assertEqual(newWage, player4.wage2)
		self.assertEqual(newHand1, player4.hand)
		self.assertEqual(newHand2, player4.hand2)
	
	def test_playersurrender(self):
		player1.surrender()

		self.assertEqual(48, player1.wallet)
	
	def test_losewage(self):
		player2.loseWage()

		self.assertEqual(46, player2.wallet)
	
	def test_clearhand(self):
		player5.clearHand()
		self.assertEqual([], player5.hand)
	
	#dealer.py
	def test_dealerhit(self):
		newCard = Card("hearts", "2", 2)
		newHand = [dcard1, dcard2, newCard]
		dealer2.hit(newCard)

		self.assertEqual(newHand, dealer2.hand)
	
	def test_dealerclearhand(self):
		dealer3.clearHand()

		self.assertEqual([], dealer3.hand)


if __name__ == '__main__':
    unittest.main()