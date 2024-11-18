# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#
#1
# YOUR CODE HERE
from math import *
import cmath
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))
if A != 0:
    if 4*A*C <= B**2:
        root1 = ((B*-1) + sqrt(B**2 - 4*A*C)) / 2*A
        root2 = ((B*-1) - sqrt(B**2 - 4*A*C)) / 2*A
        if root1 == root2:
            print(f"The root is x = {root1}")
        else:
            print(f"The roots are x = {root1} and x = {root2}")
    elif 4*A*C > B**2: 
        root1 = ((B*-1) + cmath.sqrt((B**2 - 4*A*C))) / 2*A
        root2 = ((B*-1) - cmath.sqrt((B**2 - 4*A*C))) / 2*A
        if root1 == root2:
            print(f"The root is x = {root1.real}{root1.imag}i")
        else:
            print(f"The roots are x = {root1.real} + {root1.imag}i and x = {root2.real}{root2.imag}i")
elif A == 0 and B != 0 and C!=0:
    root = (C*-1)/B
    print(f"The root is x = {root}")
elif A == 0 and B == 0:
    if C == 0:
        print("0 = 0")
    else:
        print(f"You entered an invalid combination of coefficients!")
#comments d
 