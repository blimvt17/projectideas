#diceroller: create a dice (#1-6) and roll it how many times the 
#user wants it to roll and print the outcome in %
from random import randint


def roll_dice(user_answer):
    if user_answer > 0:
        for x in range(user_answer)
            print(randint(1,6))
    else:
        print("Thanks for rolling!")

user_answer = int(input("How many times do you want to roll the dice?"))
roll_dice(user_answer)

# if dice_result == "1":
#         one_counter = one_counter + 1 
#     elif dice_result == "2":
#         two_counter = two_counter + 1
#     elif dice_result == "3":
#         three_counter = three_counter + 1
#     elif dice_result == "4":
#         four_counter = four_counter + 1
#     elif dice_result == "5":
#         five_counter = five_counter + 1
#     else:
#         six_counter = six_counter + 1

