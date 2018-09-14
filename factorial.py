# TODO: add description
def calculate_factorial(number):
  # TODO: calculate factorial of the input number and store it to result variable
  n = 1
  while number >= 1:
    n = n * number
    number = number - 1
  print(n) 

# TODO: call the function, store the output to a variable
number = int(input("Enter the number you wish to find the factorial of \n"))
calculate_factorial(number)
# TODO: print the result to the console with description
