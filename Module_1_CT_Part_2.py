#Part 2: Find the multiplication and division of two numbers

# Ask the user to input two numbers (num1 and num2)

try:
    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter a number: '))

    # Multiply them together to find the output 

    output_prod = num1 * num2
    print('The product of', num1, 'and', num2, 'is:', output_prod)

    # Divide the two numbers to find the output

    output_quot = num1 / num2
    print('The quotient of', num1, 'and', num2, 'is:', output_quot)
except ValueError:
    print("Invalid input. Please enter only numbers.")

except ZeroDivisionError:
    print('The quotient of', num1, 'and', num2, 'is: undefined')