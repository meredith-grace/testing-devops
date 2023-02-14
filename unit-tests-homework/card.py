#card object to hold information for any given card

#Unit Tests for hw1
#to run game: python3 driver.py
#to run unit tests: coverage run -m unittest discover 
#to test coverage: coverage run => then coverage report

class Card:
	def __init__(self, suit, value, numPoints):
		self.suit = suit
		self.value = value
		self.numPoints = numPoints

	def __repr__(self):
		return "% s of % s" % (self.value, self.suit)