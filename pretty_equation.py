# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Gabriel Deem
# Daniel Wu
# Ricky Alviso
# Andrew Wu
# Section: 564
# Assignment: Lab 3.15
# Date: 12/9/2023
from math import *
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))
signA = ""
signB = ""
signC = ""
Af = abs(A)
Bf = abs(B)
Cf = abs(C)
if A < 0:
    signA = "- "
if B > 0:
    signB = " + "
if B < 0:
    signB = " - "
if C > 0:
    signC = " + "
if C < 0:
    signC = " - "
#####################
if A == -1 or A == 1:
    Af = ""
if B == -1 or B == 1:
    Bf = ""
if C == 0:
    Cf = ""
#####################
if A == 0 and B == 0:
    print(f"The quadratic equation is{signC}{Cf} = 0")
elif A == 0 and B >= 0:
    print(f"The quadratic equation is {Bf}x{signC}{Cf} = 0")
elif A == 0 and B < 0:
    print(f"The quadratic equation is{signB}{Bf}x{signC}{Cf} = 0")
elif A != 0 and B == 0:
    print(f"The quadratic equation is {signA}{Af}x^2{signC}{Cf} = 0")
else:
    print(f"The quadratic equation is {signA}{Af}x^2{signB}{Bf}x{signC}{Cf} = 0")
# comment
