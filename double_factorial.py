# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#
def doublefactorial(n):
    o = 1
    if n == 0:
        o = 1
    elif n % 2 == 0:
        for a in range(2,n+1,2):
            o*=a
    elif n % 2 == 1:
        for a in range(1,n+1,2):
            o*=a
    return o
print(doublefactorial(9))
#Comment