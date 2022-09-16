num1 = input("Enter the first Number : ")
num2 = input("Enter the second Number : ")
operation = input("Enter the operation ( + or - ) : ")

if operation == '-' : result = float(num1) + float(num2)
elif operation == '+' : result = float(num1) + float(num2)
else : 
    print("invalid character!")
    quit()
    
print(result)
