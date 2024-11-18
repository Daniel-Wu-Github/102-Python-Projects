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
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
n3 = float(input("Enter number 3: "))
listN = [n1, n2, n3]
for i in listN:
    if i == n1:
        largest = i
    else:
        pass
    if i == n2:
        if i >= largest:
            largest = n2
        else:
            pass
    else:
        pass
    if i == n3:
        if i >= largest:
            largest = n3
        else:
            pass
    else:
        pass
print (f"The largest number is {largest}")
    
#comment
    
