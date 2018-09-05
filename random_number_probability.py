#importing randint function from random package
from random import randint
number_counter = [num_of_generations]

#making the random number generator with the max range being from an input
def number_generator(max_number):
    return randint(1,max_number)


def probability_calculator(num_of_generations, maximum_number):
    for i in range(num_of_generations):
        random_number_value = number_generator(maximum_number)
        number_counter = [num_of_generations]
        number_counter[random_number_value - 1] + 1 = random_number_value
        
#asking the question to set the range from 1 to max_number
max_number = int(input("What do you want the maximum number to be?")

#asking how many times the user wants to run a random number 
num_of_generations = (int(input("How many time do you want to generate random numbers?")
                            
