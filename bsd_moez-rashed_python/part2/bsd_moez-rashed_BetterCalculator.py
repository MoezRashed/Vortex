import math

print("To add use : +\nTo subtract use : -\nTo divide use : /\n"
      "To multiply use : *\nTo calculate factorial use : !\n")

op   = input("Enter the intended operation : " )

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

if   op == "+" : print("The result is : ", num1 + num2)
elif op == "-" : print("The result is : ", num1 - num2)
elif op == "/" : print("The result is : ", num1 / num2)
elif op == "*" : print("The result is : ", num1 * num2)
elif op == "!" : print("Factorial of num 1 is : ", math.factorial(num1),"\nFactorial of num 2 is : " ,math.factorial(num2))
else           : print("Invalid operator")