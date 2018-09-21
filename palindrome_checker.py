#making a palindrome checker

print('Welcome to the palindrome checker!')

#convert string into list (list comprehension)
def string_to_list(check_string):
    string_list = []
    for letter in check_string:
        string_list.append(letter)
    return (string_list)

#check by using negative index to check if letters match
def palindrome_checker(listed_string):
    if listed_string == listed_string[::-1]:
        print('It is indeed a palindrome!')
    else: 
        print('It was not a palindrome :(')

#ask user for a string to check if it's a palindrome
check_string = input('Please enter the word that you wish to check\n')

#calling string_to_list function
listed_string = string_to_list(check_string)    
palindrome_checker(listed_string)
