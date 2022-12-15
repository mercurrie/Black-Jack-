import random
import os
from art import logo

# function calculate_score takes in a list parameter and returns sum of list
def calculate_score(list):
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

# function compare_scrore takes in user and dealer's scores, compares them, and returns a string
def compare_score(user_score, dealer_score):
  if user_score > 21 and dealer_score > 21:
    return "You went over. You lose 😤"

  if user_score == dealer_score:
    return "Draw 🙃"
  elif dealer_score == 21:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 21:
    return "You win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif dealer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > dealer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

# function deal_card() returns a random number from a list 
def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    
    return random.choice(cards)

# function blackJack calls functions deal_card(), compare_score(), and calculate_score() to perform the steps of Blackjack
def blackjack():
    print(logo)
    end = True
    user = []
    dealer = []
    
    # deal 2 cards to user and dealer
    for i in range(2):
        user.append(deal_card())
        dealer.append(deal_card())
    
    # calculate score, and continue to deal cards to user as long as both scores are below 21 and user requests more cards
    while end:
        user_score = calculate_score(list = user)
        dealer_score = calculate_score(list = dealer)
        print(f'Your cards are: {user}, your current score is: {user_score}')
        print(f"The dealer's first card is: {dealer[0]}")
        
        if user_score == 21 or dealer_score == 21 or user_score > 21 :
            end = False
        else:
            user_choice = input("Would you like to be dealt another card? Input 'y' for yes and 'n' for no: ")
            if user_choice == 'y':
                user.append(deal_card())
                user_score = calculate_score(list = user)
            else:
                  end = False
                  
    # keep dealing to user until score is greater than or equal to 17
    while dealer_score != 21 and dealer_score < 17:
            dealer.append(deal_card())
            dealer_score = calculate_score(list = dealer)
        
    print(f'\nYour final hand is: {user}, your final score is: {user_score}')
    print(f"The dealer's final hand is: {dealer}, with a score of: {dealer_score}")
    print(compare_score(user_score = user_score, dealer_score = dealer_score))
    
# call Blackjack function and clear console as long as User wants to continue playing
if __name__ == '__main__':
  while input("Would you like to play a game of Blackjack? Input 'y' for yes 'n' for no: ") == 'y':
      os.system('cls')
      blackjack()