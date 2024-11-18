#1337 (or leet) is an alternative alphabet used mostly on the internet that replaces certain letters with
#other characters, such as numbers. Write a program named leet_speak.py that takes as input from the
#user a string of text, converts the words to leet, and prints the converted text. Your program must use a
#dictionary.
#Use the following letter to number conversions in your program: a > 4, e > 3, o > 0, s > 5, t > 7
#Example output (using input howdy aggies whoop):
#Enter some text: howdy aggies whoop
#In leet speak, "howdy aggies whoop" is:
#h0wdy 4ggi35 wh00p
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
leet = {'a':'4', 'e':'3', 'o':'0', 's':'5', 't':'7'}
eng = input("Enter some text:")
print(f'In leet speak, "{eng}" is: ', end="")
for i,k in enumerate(eng):
    if k in leet:
        eng = eng[:i]+leet[k]+eng[i+1:]
print(eng)
#comment