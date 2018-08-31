#letter counter

#count the number of letters in each string 
#TODO: remember the naming convention and fix the function name
def letter_counter(user_string, user_letter):
	#TODO: it counts the letter in user_string and it's doing nothing with it. return the count to the caller using return statement
    return = user_string.count(user_letter)
	
#TODO: try to count the letter using the for loop and create a test
def letter_counter_with_for_loop(input_string, search_letter):
	for (input_string, search_letter):
		result = input_string.count(search_letter)
	

#test function. this is invoked when ran with pytest.
#basically any function that has 'assert' is considered as a test function.
#ex. pytest lettercounter.py
def test_letter_counter():
	actual = letter_counter("ddaddaddadd", "a")
	expected = 3
	assert expected == actual

#main function. this is invoked when ran normally.
#ex. python lettercounter.py
if __name__ == '__main__':
	user_string = input("Please enter the word or sentence that you would like to count ")
	user_letter = input("Please enter the letter that you would like to count in your previous sentence ")
	#TODO: result is not calling the function. call the function.
	result = user_string.count(user_letter)
	'''
	TODO: when printing something to console, be informative. 
	right now, it only prints a number which user doesn't know what it's about.
	'''
	print(result)