import sys

num1 = 10
num2 = 5

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

#if __name__ == "__main__":
    # These will only run if this file is executed directly
#    print("Value of Addition:", addition(num1, num2))
#    print("Value of Subtraction:", subtraction(num1, num2)) 
#    print("Value of Multiplication:", multiplication(num1, num2))
#    print("Value of Division:", division(num1, num2))


num1 = sys.argv[1]
num2 = sys.argv[2]  
operation = sys.argv[3]

if operation == "add":
    print("Result of Addition:", addition(float(num1), float(num2)))
elif operation == "sub":
    print("Result of Subtraction:", subtraction(float(num1), float(num2)))
elif operation == "mul":
    print("Result of Multiplication:", multiplication(float(num1), float(num2)))
elif operation == "div":
    print("Result of Division:", division(float(num1), float(num2)))
else:
    print("Invalid operation")

