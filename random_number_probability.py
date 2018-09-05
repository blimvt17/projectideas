#importing randint function from random package
from random import randint
#TODO: is this how you create a list of x elements, all initialized with 0?
#see https://stackoverflow.com/questions/8528178/list-of-zeros-in-python
number_counter = [num_of_generations]

#TODO: function name should be using a verb. like do_something
#making the random number generator with the max range being from an input
def number_generator(max_number):
    return randint(1,max_number)

#TODO: function name should be using a verb. like do_something
def probability_calculator(num_of_generations, maximum_number):
            
    '''
    TODO
    think about what's going to happen in this for loop
    - get a random number and store it
    - find the nth position, where n is a random number from previous, and increment by 1
    
    google on how to assign a value to an element in a list
    '''
    for i in range(num_of_generations):
        random_number_value = number_generator(maximum_number)
        number_counter = [num_of_generations]
        number_counter[random_number_value - 1] + 1 = random_number_value
        
#asking the question to set the range from 1 to max_number
max_number = int(input("What do you want the maximum number to be?")

#asking how many times the user wants to run a random number 
#TODO: is this syntax correct? does it even run?
num_of_generations = (int(input("How many time do you want to generate random numbers?")

#TODO: are you calling the probability function?
                            
