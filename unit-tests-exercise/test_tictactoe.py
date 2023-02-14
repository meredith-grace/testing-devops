#Grace Meredith & Jeffrey Carson
#Unit Test Script

# We tested output from the function that returns a boolean (isgameover)
# we tested type errors for every function that take in parameters (isgameover, updateboard, displayboard)
# we believe we have around 70% coverage, since the other functions don't take args or return output.

from tictactoe import TicTacToe
import unittest

x = TicTacToe()
m = [["o", "o", "o"], ["4", "5", "6"], ["7", "8", "9"]] #complet game matrix top row
o = [["1", "2", "3"], ["o", "o", "o"], ["7", "8", "9"]] #complet game matrix middle row
p = [["1", "2", "3"], ["4", "5", "6"], ["o", "o", "o"]] #complet game matrix bottom row

q = [["o", "2", "3"], ["o", "5", "6"], ["o", "8", "9"]] #complet game matrix left column
r = [["1", "o", "3"], ["4", "o", "6"], ["7", "o", "9"]] #complet game matrix middle column
s = [["1", "2", "o"], ["4", "5", "o"], ["7", "8", "o"]] #complet game matrix right column

t = [["o", "2", "3"], ["4", "o", "6"], ["7", "8", "o"]] #complet game matrix diagnol 1
u = [["1", "2", "o"], ["4", "o", "6"], ["o", "8", "9"]] #complet game matrix diagnol 2

n = [["o", "2", "o"], ["4", "5", "6"], ["7", "8", "9"]] #not complete game matrix

class TestTicTacToe(unittest.TestCase):
	def test_GameOver(self):
		self.assertTrue(x.isGameOver(m))
		self.assertTrue(x.isGameOver(o))
		self.assertTrue(x.isGameOver(p))
		self.assertTrue(x.isGameOver(q))
		self.assertTrue(x.isGameOver(r))
		self.assertTrue(x.isGameOver(s))
		self.assertTrue(x.isGameOver(t))
		self.assertTrue(x.isGameOver(u))
		self.assertFalse(x.isGameOver(n))

		with self.assertRaises(TypeError):
			x.isGameOver(0)

	def test_UpdateBoard(self):
		with self.assertRaises(TypeError):
			x.updateBoard(0, "o")

		self.assertTrue(x.updateBoard("1", "o"))
		self.assertTrue(x.updateBoard("2", "o"))
		self.assertTrue(x.updateBoard("3", "o"))
		self.assertTrue(x.updateBoard("4", "o"))
		self.assertTrue(x.updateBoard("5", "o"))
		self.assertTrue(x.updateBoard("6", "o"))
		self.assertTrue(x.updateBoard("7", "o"))
		self.assertTrue(x.updateBoard("8", "o"))
		self.assertTrue(x.updateBoard("9", "o"))
		self.assertFalse(x.updateBoard("j", "o"))

	def test_DisplayBoard(self):
		with self.assertRaises(TypeError):
			x.displayBoard(0)

	def test_switchturn(self):
		self.assertEqual(x.switchTurn("o"), "x")
		self.assertEqual(x.switchTurn("x"), "o")


if __name__ == '__main__':
    unittest.main()