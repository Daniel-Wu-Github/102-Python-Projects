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
#
import math

def triA (side):
    area = (side**2)*(math.sqrt(3)/4)
    return(area)

def squareA (side):
    area = (side**2)
    return(area)
    
def pentA (side):
    area = 0.25*(side**2)*(math.sqrt(5*(5+2*math.sqrt(5))))
    return(area)
  
def dodeA (side):
    area = 3*(side**2)*(2+math.sqrt(3))
    return(area)  

sideI = float(input("Please enter the side length:"))
print(f"A triangle with side {sideI:.2f} has area {triA(sideI):.3f}")
print(f"A square with side {sideI:.2f} has area {squareA(sideI):.3f}")
print(f"A pentagon with side {sideI:.2f} has area {pentA(sideI):.3f}")
print(f"A dodecagon with side {sideI:.2f} has area {dodeA(sideI):.3f}")

