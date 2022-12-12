import random
import os
from art import logo

# function calculateScore takes in a list parameter and returns sum of list
def calculateScore(list):
    count = sum(list)

    if count == 21:
        return 21
    elif count > 21:
        for num in list:
            if num == 11:
                list.remove(num)
                list.append(1)
                count = sum(list)
    
    return count

# function compareScrore takes in user and dealer's scores, compares them, and returns a string
def compareScore(userScore, dealerScore):
  if userScore > 21 and dealerScore > 21:
    return "You went over. You lose 😤"

  if userScore == dealerScore:
    return "Draw 🙃"
  elif dealerScore == 0:
    return "Lose, opponent has Blackjack 😱"
  elif userScore == 0:
    return "You win with a Blackjack 😎"
  elif userScore > 21:
    return "You went over. You lose 😭"
  elif dealerScore > 21:
    return "Opponent went over. You win 😁"
  elif userScore > dealerScore:
    return "You win 😃"
  else:
    return "You lose 😤"

# function dealCard returns a random number from a list 
def dealCard():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    
    return random.choice(cards)

# function blackJack calls functions dealCard(), compareScore(), and calculateScore() to perform the steps of Blackjack
def blackJack():
    print(logo)
    end = True
    user = []
    dealer = []
    
    for i in range(0,2):
        user.append(dealCard())
        dealer.append(dealCard())
    
    while end:
        userScore = calculateScore(user)
        dealerScore = calculateScore(dealer)
        print(f'Your cards are: {user}, your current score is: {userScore}')
        print(f"The dealer's first card is: {dealer[0]}")
        
        if userScore == 21 or dealerScore == 21 or userScore > 21 :
            end = False
        else:
            userHit = input("Would you like to be dealt another card? Input 'y' for yes and 'n' for no: ")
            if userHit == 'y':
                user.append(dealCard())
                userScore = calculateScore(user)
            else:
                  end = False
        
    while dealerScore != 21 and dealerScore < 17:
            dealer.append(dealCard())
            dealerScore = calculateScore(dealer)
        
    print(f'\nYour final hand is: {user}, your final score is: {userScore}')
    print(f"The dealer's final hand is: {dealer}, with a score of: {dealerScore}")
    print(compareScore(userScore, dealerScore))
    
# call Blackjack function and clear console as long as User wants to continue playing
while input("Would you like to play a game of Blackjack? Input 'y' for yes 'n' for no: ") == 'y':
    os.system('cls')
    blackJack()