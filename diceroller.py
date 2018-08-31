#diceroller: create a dice (#1-6) and roll it how many times the 
#user wants it to roll and print the outcome in %
from random import randint

#TODO: function name should have verb, like roll_dice
#TODO: function should generate a random number and return it
def dice():
    #TODO: print is not closed
    print(randint(1,6)
    
#TODO: instead of yes/no option, get a number from the user and roll the dice that many times
#TODO: variable name is not appropriate. it's not an answer
user_answer = input("Do you want to roll the dice one hundred times? (yes or no)")
for x in range(100):
    if user_answer == "yes":
        dice()
    else: 
        print("Thank you for using the dice roller")

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

