#holds all methods for game-play during each round.

#Unit Tests for hw1
#to run game: python3 driver.py
#to run unit tests: coverage run -m unittest discover 
#to test coverage: coverage run => then coverage report

from deck import Deck
from dealer import Dealer
from player import Player

deck = Deck()

def startGame(dealer = None, player = None):
    deck.shuffle()

    if isFirstRound(dealer, player):
        wage = getWager(50)
        dealer, player = dealCards(deck, wage, 50)
    else:
        player.wage = getWager(player.wallet)
        dealer.clearHand()
        player.clearHand()
        player.hand = [deck.draw(), deck.draw()]
        dealer.hand = [deck.draw(), deck.draw()]
    player.revealHand()
    print("\n\n")
    dealer.revealFirstCard()
    print("\n\n")

    makeDecision(dealer, player)

    return dealer, player


def dealCards(deck, wage, wallet):
    d = Dealer([deck.draw(), deck.draw()])
    p = Player([deck.draw(), deck.draw()], wage, wallet)

    return d, p

def makeDecision(dealer, player):
    while True:
        print("\nOkay, now you have your cards, time to choose your next move. Would you like to 'stand', 'hit', 'double down', 'split', or 'surrender'?")
        choice = input()

        if 'st' in choice:
            player.stand()
            finalResult(dealer, player)
            break
        elif 'h' in choice:
            player.hit(deck.draw())
            player.revealHand()
            while True:
                print("Would you like to hit again, or stand?")
                c = input()
                if "h" in c:
                    player.hit(deck.draw())
                    player.revealHand()
                elif "s" in c:
                    player.stand()
                    finalResult(dealer, player)
                    break
            break
        elif 'do' in choice:
            player.doubleDown(deck.draw())
            player.revealHand()
            finalResult(dealer, player)
            break
        elif 'sp' in choice:
            if player.wage != player.wallet and player.hand[0].numPoints == player.hand[1].numPoints:
                print("P\nlease select a second Wage to split your hand")
                w2 = getWager(player.wallet - player.wage) #subtract first wage from wallet to see how much is left available to bet for second wage
                player.split(w2, deck.draw(), deck.draw())
                player.revealSplitHands()
                splitResult(dealer, player)
                break
            else:
                print("\nSorry, either: you bet all your money for your current hand and you don't have enough for a second wage.\n or you don't have a matching pair to split \n Please Select another option")
        elif 'su' in choice:
            player.surrender()
            break


def dealersTurn(dealer):
    dealer.revealEntireHand()
    subTotal = sumHand(dealer.hand)

    if subTotal >= 17:
        dealer.stand
    else:
        dealer.hit(deck.draw())
        dealer.revealEntireHand()

    return sumHand(dealer.hand)

def finalResult(dealer, player, split=False):
    dealerTotal = dealersTurn(dealer)
    playerTotal = 0
    if split:
        playerTotal = sumHand(player.hand2)
    else:
        playerTotal = sumHand(player.hand)
    winner = ""

    if hasBlackJack(playerTotal):
        print("\nPlayer got a BlackJack, you win!!")
        winner = "player"
    elif hasBlackJack(dealerTotal):
        print("\nDealer got a BlackJack, you lose :(")
        winner = "dealer"
    else:
        winner = checkWinner(dealerTotal, playerTotal)

    if winner == "player":
        print("\nPlayer's hand defeats the dealers! you win!!")
        if split:
            dealer.payout(player.wage2, player.wallet)
            player.wallet = player.wallet + player.wage2
        else:
            dealer.payout(player.wage, player.wallet)
            player.wallet = player.wallet + player.wage
    else:
        print("\nSorry, the dealer's hand defeated yours, you lose :(")
        player.loseWage(split)

def splitResult(dealer, player):
    print("\nResult of First Hand: ")
    finalResult(dealer, player)

    print("\nResult of Second Hand: ")
    finalResult(dealer, player, True)

def sumHand(hand):
    s=0
    for h in hand:
        s += h.numPoints
    s = checkAce(hand, s)
    return s

def checkAce(hand, s): #Ace is default valued as 11, but if the sum of the players/dealers deck is over 21, than Ace will be valued as 1.
    for h in hand:
        if h.value == "A" and s>21:
            s -= 10
    return s

def getWager(wallet=50):
    print("\nYour wallet has $" + str(wallet) + " available to bet. How much would you like to wager?")
    while True:
        wage = int(input())
        if not validWage(wage, wallet):
            print("Sorry, you cannot afford that wage")
        else:
            break
    return wage

def isFirstRound(dealer, player):
    return dealer is None or player is None

def validWage(wage, wallet):
    return wage <= wallet and wage > 0

def hasBlackJack(num):
    return num == 21

def checkWinner(dtotal, ptotal):
    if ptotal > 21:
        return "dealer"
    elif dtotal > 21:
        return "player"
    elif ptotal >= dtotal:
        return "player"
    else:
        return "dealer"
