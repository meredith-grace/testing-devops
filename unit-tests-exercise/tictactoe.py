#Grace Meredith & Jeffrey Carson
#Activity 3 Pair 14
#07 February 2022


class TicTacToe():

	__gameboard =[["1", "2", "3"], 
		["4", "5", "6"],
		["7", "8", "9"]]

	__winner = None

	def playTTT(self):
		self.__intro()
		count = 0
		turn = "x"

		while not self.isGameOver(self.__gameboard) and count < 9:
			successful = False
			self.displayBoard(self.__gameboard)
			while not successful:
				pos = input()
				successful = self.updateBoard(pos, turn)
			turn = self.switchTurn(turn)
			count+=1

		if self.__winner is not None and "x" in self.__winner:
			print("Player 1 wins")
		elif self.__winner is not None and "o" in self.__winner:
			print("Player 2 Wins")
		else:
			print("It's a tie")

	def isGameOver(self, matrix):
		
		if matrix[0][0] == matrix[0][1] == matrix[0][2]: #top row win
			self.__winner = matrix[0][0]
			return True
		elif matrix[1][0] == matrix[1][1] == matrix[1][2]: #middle row win
			self.__winner = matrix[1][0]
			return True
		elif matrix[2][0] == matrix[2][1] == matrix[2][2]: #bottom row win
			self.__winner = matrix[2][0]
			return True



		elif matrix[0][0] == matrix[1][0] == matrix[2][0]: #left column win
			self.__winner = matrix[0][0]
			return True
		elif matrix[0][1] == matrix[1][1] == matrix[2][1]: #middle column win
			self.__winner = matrix[0][1]
			return True
		elif matrix[0][2] == matrix[1][2] == matrix[2][2]: #bottom column win
			self.__winner = matrix[0][2]
			return True



		elif matrix[0][0] == matrix[1][1] == matrix[2][2]: 
			self.__winner = matrix[0][0]
			return True
		elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
			self.__winner = matrix[0][0]
			return True






	def updateBoard(self, pos, turn):

		if "1" in pos and self.__gameboard[0][0] == "1":
			self.__gameboard[0][0] = turn
			return True
		elif "2" in pos and self.__gameboard[0][1] == "2":
			self.__gameboard[0][1] = turn
			return True
		elif "3" in pos and self.__gameboard[0][2] == "3":
			self.__gameboard[0][2] = turn
			return True
		elif "4" in pos and self.__gameboard[1][0] == "4":
			self.__gameboard[1][0] = turn
			return True
		elif "5" in pos and self.__gameboard[1][1] == "5":
			self.__gameboard[1][1] = turn
			return True
		elif "6" in pos and self.__gameboard[1][2] == "6":
			self.__gameboard[1][2] = turn
			return True 
		elif "7" in pos and self.__gameboard[2][0] == "7":
			self.__gameboard[2][0] = turn
			return True
		elif "8" in pos and self.__gameboard[2][1] == "8":
			self.__gameboard[2][1] = turn
			return True
		elif "9" in pos and self.__gameboard[2][2] == "9":
			self.__gameboard[2][2] = turn
			return True
		else:
			print("not valid position, try again")
			return False



	def displayBoard(self, matrix):
		for x in matrix:
			print(str(x))

	def switchTurn(self, turn):
		if "o" in turn:
			return "x"
		else:
			return "o"

	def __intro(self):
		print("Welcome to tic tac toe")
		print("player one is x, player two is o")
		print("Just enter the desired position as displayed in the gameboard")

def main():
	x = TicTacToe()
	x.playTTT()


if __name__ == "__main__":
	main()




