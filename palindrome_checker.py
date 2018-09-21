#making a palindrome checker

#TODO always define functions and classes first. then start the main business logic
print('Welcome to the palindrome checker!')

#TODO remember the naming convention. function names usually start with a verb
#convert string into list (list comprehension)
def string_to_list(check_string):
    string_list = []
    for letter in check_string:
        string_list.append(letter)
    #TODO remove parenthesis in return statement
    return (string_list)

#TODO remember the naming convention. function names usually start with a verb
#TODO this function should expect a string, not a list of characters
#check by using negative index to check if letters match
def palindrome_checker(listed_string):
    if listed_string == listed_string[::-1]:
        #this function should return true/false. this prints should be used by the caller of this function.
        print('It is indeed a palindrome!')
    else: 
        print('It was not a palindrome :(')

#ask user for a string to check if it's a palindrome
check_string = input('Please enter the word that you wish to check\n')

#TODO think about the responsibility. if some company wants to call the palindrom checker, now they need to care about turning string into a list of characters and we don't want that. 
#calling string_to_list function
listed_string = string_to_list(check_string)    
palindrome_checker(listed_string)
