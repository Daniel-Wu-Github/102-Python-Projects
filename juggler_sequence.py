# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#
num = int(input("Enter a positive integer:"))
k = 0
print(f"The Juggler sequence starting at {num} is:")
if num == 1:
    print(f"{num}", end = " ")
else:
    print(f"{num}", end = ", ")
while num != 1:
    if num % 2 == 0:
        num = int(num ** (1/2))
        if num == 1:
            print(f"{num}", end = " ")
        else:
            print(f"{num}", end = ", ")
    elif num % 2 == 1:
        num = int(num ** (3/2))
        if num == 1:
            print(f"{num}", end = " ")
        else:
            print(f"{num}", end = ", ")
    k+=1
print(f"It took {k} iterations to reach 1")
#Example output (using input 7):
#Enter a positive integer: 7
#The Juggler sequence starting at 7 is:
#7, 18, 4, 2, 1
#It took 4 iterations to reach 1