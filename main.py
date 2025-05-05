import random
from os import remove
import art


def pick_card():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user,computer):
    if computer==0:
        return "Computer Wins with a Blackjack!"

    elif user==0:
        return "User Wins With a Blackjack"

    elif user==computer:
        return "Its a Draw!"

    elif user>21:
        return "User Went Over! Computer Wins!"

    elif computer>21:
        return "Computer Went Over! User Wins!"

    elif user>computer:
        return "User Wins"

    elif user<computer:
        return "Computer Wins"

def play_game():
    print(art.logo)
    user_cards=[]
    computer_cards=[]
    is_game_over=False
    user_score=-1
    computer_score=-1

    for _ in range(2):
        user_cards.append(pick_card())
        computer_cards.append(pick_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}  Your Score:{user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            choice = input("Type 'y' to draw another card, 'n' To stop:").lower()
            if choice=="y":
                user_cards.append(pick_card())
            else:
                is_game_over=True

    while computer_score !=0 and computer_score<17:
        computer_cards.append(pick_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your Final Cards:{user_cards}  | Your Score:{user_score}")
    print(f"Computer Final Cards:{computer_cards}  | Computer's Score:{computer_score}")


    print(compare(user_score,computer_score))
while input("Do You Wish To Play a Game of Blackjack?(y/n)").lower()=="y":
    print("\n"*20)
    play_game()

