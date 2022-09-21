print("Guess an animal, you have 3 guesses!\n")

secret = "giraffe"
guess = ""
numOfGuesses = 3
found = False

while numOfGuesses > 0:
    if numOfGuesses == 1:   print("You have only",numOfGuesses,"guess left!\n")
    else :                  print("You have",numOfGuesses,"guesses left!\n")

    guess = input("Enter your guess : ")

    if guess == secret :
        found = True
        break
    numOfGuesses-=1

if found == True : print("You win!")
else             : print("You lost!")

