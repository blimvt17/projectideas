#rps game - user vs the computer 
import random 

print("I challenge you to a game of Rock Paper Scissors")
tie = "It's a tie!"
win = "You won!"
loss = "You lose :("
choice = ['rock', 'paper', 'scissors']

player = input("Please (r)ock, (p)aper, or (s)cissors")

computerchoice = random.choice(choice)

if (player == "r" and computerchoice == "rock"):
    print(tie) 
elif (player == "r" and computerchoice == "scissors"):
    print(win)
elif (player =="r" and computerchoice == "paper"):
    print(loss)
elif (player == "p" and computerchoice == "rock"):
    print(win)
elif (player =="p" and computerchoice == "scissors"):
    print(loss)
elif (player == "p" and computerchoice == "paper"):
    print(tie)
elif (player =="s" and computerchoice == "paper"):
    print(win)
elif (player =="s" and computerchoice == "rock"):
    print(loss)
else: 
    print(tie)

