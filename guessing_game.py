# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
secret = 27
guesses = 0
def pHint():
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
def count():
    print(f"You guessed it! It took you {guesses+1} guesses.")
def isValid(guess):
    if guess.is_integer() and guess >= 1:
        return True
    else:
        return False
def convert(guess):
    try:
        float(guess)
        return float(guess)
    except ValueError:
        return -1.0
    
pHint()
guess = input("What is your guess? ")
while convert(guess) != secret:
    if isValid(convert(guess)) == False:
        guess = input("Bad input! Try again: ")
    else:
        if convert(guess) > secret:
                print("Too high!")
                guesses+=1
        else:
            print("Too low!")
            guesses+=1
        guess = input("What is your guess? ")
count()
#Comment