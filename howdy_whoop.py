# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#
a = int(input("Enter an integer:"))
b = int(input("Enter another integer:"))
for k in range(1,101):
    if (k%a == 0) and (k%b == 0):
        print("Howdy Whoop")
    elif (k%a != 0) and (k%b == 0):
        print("Whoop")
    elif k%a == 0:
        print("Howdy")
    else:
        print(k)
#Comment