
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":  translation = translation + 'V'
        else : translation = translation + letter.lower()
    return translation

print(translate(input("Please enter a sentence : ")))