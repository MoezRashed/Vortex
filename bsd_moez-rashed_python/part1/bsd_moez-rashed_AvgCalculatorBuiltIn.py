input_string = input('Enter numbers separated by space ')
print("\n")

numbers = input_string.split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print("Sum = ", sum(numbers))
print("Average = ", sum(numbers) / len(numbers))