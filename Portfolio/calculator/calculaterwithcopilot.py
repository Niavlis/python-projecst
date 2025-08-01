# This is a simple calculator program that performs basic arithmetic operations
# It takes two numbers and a type of calculation as input from the user
#this part asks what numbers to calculate
num1 = input("enter number 1: ")
num2 = input("enter number 2: ")

#this makes the inputs numbers (integers)
num1 = int(num1)
num2 = int(num2)
#here it asks what type of calculation to do
type = input("Enter the type of calculation (sum, product, minus, division): ")
if type not in ['sum', 'product', 'minus', 'division']:
    print("Invalid calculation type. Please enter one of: sum, product, minus, division.")
    exit()
#here it checks what to do and does it
if type == 'sum':
    result = num1 + num2
elif type == 'product':
    result = num1 * num2
elif type == 'minus':
    result = num1 - num2
elif type == 'division':
    result = num1 / num2
#this says what the result is
print("the result of the", type, "is", result)

