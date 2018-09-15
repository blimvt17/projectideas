#game of rock paper scissors - user vs the computer 
import random 
 
#making a function called play which tests the conditionals of rps logic. 
def play(choice, computer_choice):
    
    display_tie = 'It's a tie!'
    display_win = 'You won!'
    display_loss = 'You lose :('
    error_message = 'Invalid choice'

    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'

    if choice == computer_choice: 
        return display_tie
    elif (choice == rock and computer_choice == scissors):
        return display_win
    elif (choice == rock and computer_choice == paper):
        return display_loss
    elif (choice == paper and computer_choice == rock):
        return display_win
    elif (choice == paper and computer_choice == scissors):
        return display_loss
    elif (choice == scissors and computer_choice == paper):
        return display_win
    elif (choice == scissors and computer_choice == rock):
        return display_loss
    else: 
        return error_message
        
#added a for loop to running the function so you can specify in code how many times you want to play - simply change the value in the range()
print('I challenge you to a game of Rock Paper Scissors!')
keep_playing = 'Yes'

while keep_playing == 'Yes':
    
# for x in range(1):
    # print('I challenge you to a game of Rock Paper Scissors!')
    player_choice = input('Please choose rock, paper, scissors by typing the full word\n')
    
    #I want to exit program if they don't type the choice correctly 
    valid_choices = ['rock', 'paper', 'scissors']
    
    if player_choice not in valid_choices:
        print('Please correctly type rock, paper or scissors')
    
    else: 
        computer_choice = random.choice(valid_choices)
        result = play(player_choice, computer_choice)
        print('The computer put out ' + computer_choice + '! ' + result)
    keep_playing = input('Do you want to keep playing? Enter 'Yes' to keep playing \n')
print('Thanks for playing!') 
#test code that tests rock (player_choice) against the computers_choice
# print('I challenge you to a game of Rock Paper Scissors')
# player_choice = 'r'
# computer_choice = 'r'
# result = play(player_choice, computer_choice)
# print(result)

# print('I challenge you to a game of Rock Paper Scissors')
# player_choice = 'r'
# computer_choice = 'p'
# result = play(player_choice, computer_choice)
# print(result)

# print('I challenge you to a game of Rock Paper Scissors')
# player_choice = 'r'
# computer_choice = 's'
# result = play(player_choice, computer_choice)
# print(result)
    




