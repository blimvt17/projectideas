#given an input of numbers
#output the highest number 
    

# def number_splitter(user_given_numbers):
#     return list(map(int, user_given_numbers.split(', ')))


def highest_number_finder(user_given_numbers):
    # listed_numbers = number_splitter(user_given_numbers)
    listed_numbers = [int(x) for x in user_given_numbers().split()]
    max_number = None
    max_number = max(listed_numbers)
    return max_number
    

#ask user for how many numbers to put in list 
user_given_numbers = (input('Please enter the number in the following format: #, #, #, #, etc..'))
found_max_number = highest_number_finder(user_given_numbers)
print(found_max_number)
