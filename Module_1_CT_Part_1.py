# Module 1 Critical Thinking Assignment

#Part 1: Find the addition and subtraction of two numbers

# Ask the user to input two numbers (num1 and num2)
try:
    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter a number: '))

# add them together to find the output 
    output_sum = num1 + num2
    print('The sum of', num1, 'and', num2, 'is:', output_sum)

# subtract the two numbers to find the output
    output_diff = num1 - num2
    print('The difference of', num1, 'and', num2, 'is:', output_diff)
    
except ValueError:
    print("Invalid input. Please enter only numbers.")

