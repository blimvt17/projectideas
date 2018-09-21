#diceroller: create a dice (#1-6) and roll it how many times the 
#user wants it to roll and print the outcome in %
from random import randint


def roll_dice():
    return randint(1,6)

# there is a display_dice_probability function
def display_dice_probability(user_answer):
    
    one_counter = 0 
    two_counter = 0 
    three_counter = 0 
    four_counter = 0 
    five_counter = 0 
    six_counter = 0 
        
    for x in range(user_answer):

        # DDP calls the roll_dice function
        dice_result = roll_dice()

        # DDP increments the counter for the number returned from roll_dice function
        if dice_result == 1:
            one_counter = one_counter + 1 
        elif dice_result == 2:
            two_counter = two_counter + 1
        elif dice_result == 3:
            three_counter = three_counter + 1
        elif dice_result == 4:
            four_counter = four_counter + 1
        elif dice_result == 5:
            five_counter = five_counter + 1
        else:
            six_counter = six_counter + 1   
    
    #making a range for counter
    dice_count = [one_counter, two_counter, three_counter, four_counter, five_counter, six_counter]

    # after rolling the dice for x number of times, it prints all the counters
    for i in range[dice_count]:
        print("You've rolled the number 1 " + str(dice_count) + "times!")
    

# DDP function takes an input - number, how many times you want to roll the dice
user_answer = int(input("How many times do you want to roll the dice?"))
display_dice_probability(user_answer)