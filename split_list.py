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
left = 0
right = 0
num = input("Enter numbers:")
numList = num.split()
for i in range(len(numList)):
    numList[i] = int(numList[i])
for i2 in numList:
    lTemp = left.copy()
    rTemp = right.copy()
    left = 0
    for j in numList[:i2]:
        left += j
        #print(left)
    for k in numList[i2:]:
        right += k
        print(right)
    listL = numList[:i2]
    listR = numList[i2:]
    if left == right:
        print(f"Left: {listL}")
        print(f"Right: {listR}")
        print(f"Both sum to {left}")
        break
if lTemp != rTemp:
    print("Cannot split evenly")
#comment