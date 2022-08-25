import random
from blackJackLogo import logo
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
word_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

word_user_cards = []
word_computer_cards = []

number_user_cards = [0, 0, 0, 0, 0]
number_computer_cards = [0, 0, 0, 0, 0]

should_finish = False

def convert_to_number():
    for i in range(len(word_user_cards)):
        for position_1 in range(len(word_cards)):
            if word_user_cards[i] == word_cards[position_1]:
                number_user_cards[i] = cards[position_1]

    for j in range(len(word_computer_cards)):
        for position_2 in range(len(word_cards)):
            if word_computer_cards[j] == word_cards[position_2]:
                number_computer_cards[j] = cards[position_2]

def convert_score():
    if "A" in word_computer_cards and len(word_computer_cards) == 3:
        for number1 in number_computer_cards:
            if number1 == 11:
                number1 = 1
            
    if "A" in word_user_cards and len(word_user_cards) == 3:
        for number2 in number_user_cards:
            if number2 == 11:
                number2 = 1

print(logo)

answer = input("Do you want to play blackjack game? Type \"y\" or \"n\": ")
if answer == "y":
    want_to_play = True
elif answer == "n":
    print("Good luck!")

def cal_score():
    global user_score 
    user_score= sum(number_user_cards)
    global computer_score 
    computer_score= sum(number_computer_cards)

    if user_score == 21 and len(word_user_cards) == 2:
        user_score = 0

    if computer_score == 21 and len(word_computer_cards) == 2:
        computer_score = 0

def compare_cards(user_score, computer_score):
    if user_score == 0 and computer_score != 0:
        print("You win with blackjack!")
    elif computer_score == 0 and user_score != 0:
        print("You lose, your opponent wins with blackjack!")
    elif user_score == 22 and len(number_user_cards) == 2 and computer_score != 22 and len(number_computer_cards) == 2:
        print("You win with double blackjack!")
    elif computer_score == 22 and len(number_computer_cards) == 2 and user_score != 22 and len(number_user_cards) == 2:
        print("You lose, your opponent wins with double blackjack!")
    elif ((user_score > 21 or user_score < 13) and (computer_score >= 13 or computer_score <= 21)):
        print("You lose! Your score went over")
    elif((computer_score > 21 or computer_score < 13) and (user_score <=21 or user_score >= 13)):
        print("You win! Computer's score went over")
    elif user_score > computer_score:
        print("You win!")
    elif computer_score > user_score:
        print("You lose!")
    elif ((user_score < 13 and user_score > 21) or (computer_score < 13 and computer_score > 21)): 
        print("Draws")
    elif user_score == computer_score: 
        print("Draws")

while want_to_play == True:
    
    while should_finish == False:
        
        for _ in range(2):
            word_user_cards.append(random.choice(word_cards))
            word_computer_cards.append(random.choice(word_cards))

        convert_to_number()

        print(f"Your cards is {word_user_cards}, your current score is {sum(number_user_cards)}")
        print(f"Computer's first card is [{word_computer_cards[0]}, _]")

        while sum(number_computer_cards) < 13 and len(word_computer_cards) < 5:
            word_computer_cards.append(random.choice(word_cards))
            convert_to_number()

        anwser1 = input("Do you want to hand card? Type \"y\" or \"n\": ")
        if anwser1 == "y":
            anwser2 = 'y'
            while anwser2 == 'y':
                word_user_cards.append(random.choice(word_cards))
                convert_to_number()
                print(f"Your cards is {word_user_cards}, your current score is {sum(number_user_cards)}")
                anwser2 = input("Do you want to continue hand card? Type \"y\" or \"n\": ")

        should_finish = True

    convert_score()
    cal_score()
    print(f"Your cards is {word_user_cards}, computer's card is {word_computer_cards} and {computer_score} score")
    compare_cards(user_score, computer_score)

    answer = input("Do you want to play a new blackjack game? Type \"y\" or \"n\": ")
    if answer == "y":
        want_to_play = True
        should_finish = False
        word_user_cards.clear()
        word_computer_cards.clear()
        number_user_cards = [0, 0, 0, 0, 0]
        number_computer_cards = [0, 0, 0, 0, 0]
        os.system("cls")
        print(logo)
    elif answer == "n":
        want_to_play = False
        os.system("cls")
        print("Good luck! You go have fun!")







