# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#
#
# YOUR CODE HERE
#
def produceGadgets (c):
    days = 1
    gadgets = 0
    while days <= c and days < 11:
        gadgets += 10
        days += 1
    while days <= c and days < 51:
        gadgets += days
        days += 1
    while days <= c and days < 101:
        gadgets += 50
        days += 1
    if days == 101:
        pass
    return (days, gadgets)

dayInput = int(input("Please enter a positive value for day: "))
days, gadgets = produceGadgets (dayInput)
if dayInput >= 0:
    print(f"The sum total number of gadgets produced on day {dayInput} is {gadgets}")
else:
    print("You entered an invalid number!")

 #comment to self       
    