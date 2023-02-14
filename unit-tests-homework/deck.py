from card import Card
#Deck class which will hold a deck of cards for the players

#Unit Tests for hw1
#to run game: python3 driver.py
#to run unit tests: coverage run -m unittest discover 
#to test coverage: coverage run => then coverage report

import random
from card import Card

class Deck:
	def __init__(self):
		suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
		cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

		self.deck = []
		self.index = -1 #to keep track of which card is 'on top' of the pile, basically treat the deck like a stack

		for card in cards:
			for suit in suits:
				self.deck.append(Card(suit, card, cards_values[card]))

	def shuffle(self):
		random.shuffle(self.deck)
		self.index = -1

	def remove(self, card):
		self.deck.remove(card)
	
	def draw(self):
		self.index += 1
		return self.deck[self.index]