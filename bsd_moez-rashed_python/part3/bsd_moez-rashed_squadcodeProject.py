import random
hard_core_words=("water","orange","ant","grass")
secret_word=random.choice(hard_core_words).lower()
letters=""
failcount= 8
while failcount>0:
    guess=input("Enter a letter: ")
    if guess in secret_word:
        print("Correct!")
        letters=letters+guess
    else:
        failcount-=1
        print("Incorrect")
    ##a
    # letters=letters+guess
    wrongletters= 0
    for letter in secret_word:
        if letter in letters:
            print(f"{letter}",end=" ")
        else:
            print("_",end=" ")
            wrongletters +=1
    if wrongletters==0:
        print(f"The word was {secret_word}")
        break
else:
    print("You Lost")