#Grace Meredith
#Homework 1: BlackJack
#Due 13 February 2022

#Unit Tests for hw1
#to run game: python3 driver.py
#to run unit tests: coverage run -m unittest discover 
#to test coverage: coverage run => then coverage report

from game import *

def intro():
    print("Welcome to blackjack!! Let's Start!")
    print("if you aren't familiar with the rules, refer to this guide: https://www.blackjackapprenticeship.com/how-to-play-blackjack/")
    print("---------------------------------------------------------------------------------------------------------------------------")
    d, p = startGame()
    if not wentBroke(p.wallet):
        playAgain(d, p)
    else:
        print("Sorry, you lost all your money.")

def playAgain(d, p):
    choice = "y"
    while canPlayAgain(choice) and not wentBroke(p.wallet):
        print("\nPlay Again? Enter 'y' to play again, or any other key to exit")
        print("Note: if you choose to exit now, all saved data will be lost, i.e your wallet will reset")
        choice = input()

        if canPlayAgain(choice):
            print("\n\n\n\n\n\n\n\n\n\n")
            print("---------------------------------------------------------------------------------------------------------------------------")
            d, p = startGame(d, p)
        if wentBroke():
            print("Sorry, you lost all your money.")

def wentBroke(wallet):
    return wallet <= 0

def canPlayAgain(choice):
    return "y" in choice

def main():
    intro()

if __name__ == "__main__":
    main()