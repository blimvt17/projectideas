#importing randint function from random package
from random import randint

#making the random number generator with the max range being from an input
def generate_random_numbers(max_number):
    return randint(1,max_number)
    

def calculate_probability(num_of_generations, max_number):
    number_counter = [0]*max_number            
    probability_list = list()
    '''
    TODO
    think about what's going to happen in this for loop
    - get a random number and store it
    - find the nth position, where n is a random number from previous, and increment by 1
    
    google on how to assign a value to an element in a list
    '''
    for i in range(num_of_generations):
        random_number_value = generate_random_numbers(max_number)
        number_counter[(random_number_value-1)] = number_counter[(random_number_value-1)] +1
        #printing result?
    for i in range(max_number):
        probability_list.append(str(round(number_counter[i-1] / num_of_generations * 100, 2))+"%")
    return probability_list
    


#asking how many times the user wants to run a random number 
max_number = int(input("What do you want the maximum number to be?"))

num_of_generations = int(input("How many time do you want to generate random numbers?"))

#calling the probability function
probability_list = calculate_probability(num_of_generations,max_number)
print(probability_list)                          
