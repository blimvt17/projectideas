#letter counter, count the number of letters in each string 

def lettercounter(user_string, user_letter):
    user_string.count(user_letter)

user_string = input("Please enter the word or sentence that you would like to count ")
user_letter = input("Please enter the letter that you would like to count in your previous sentence ")
result = user_string.count(user_letter)
print(result)