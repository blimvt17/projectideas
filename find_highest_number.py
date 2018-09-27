#given an input of numbers
#output the highest number 
    
def number_splitter(list_of_numbers):
    return list(map(int, list_of_numbers.split(', ')))

def highest_number_finder(list_of_numbers):
    split_numbers = number_splitter(list_of_numbers)
    max_number = None
    for numbers in split_numbers: 
        if split_numbers[numbers] > max_number:
            max_number = split_numbers[numbers] 
        else:
            continue

    
    

#ask user for how many numbers to put in list 
list_of_numbers = (input('Please enter the number in the following format: #, #, #, #, etc..\n'))
highest_number_finder(list_of_numbers)
