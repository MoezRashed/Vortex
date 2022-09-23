import random

myWords = {
    1 : "elephant",
    2 : "orange",
    3 : "ant",
    4 : "water",
    5 : "earth"
}
guess = random.choice(myWords).lower()

def check():
    for i in guess:
        if i in right:
            print(i, end=' ')
        else:
            print('_', end=' ')
    print ("\n")
  
right = [] 
wrong = []
chances = 8 

while chances > 0:
    check()
    letter = input ("Enter your guess : ").lower()

    if letter in right or letter in wrong:
            print("You have already guessed", letter,"sorry")
            chances-=1
            continue
    elif len(letter) == 0:
            print("Please type a letter")
            continue
    elif len(letter) > 1:
        raise Exception("Please enter one letter only !")

    if letter in guess:
        right.append(letter)
        print("Nice guess, Go on!")
        if len(right) == len(guess):
            break
    else:
        wrong.append(letter)
        print ("Sorry, the word doesn't contain", letter,"you have",8-len(wrong),"guesses left")
        chances-=1


if chances == 0:
    print ("GAME OVER!, your word was",guess.upper())
else:
    print("Coungratulations! You have won, your word was", guess)