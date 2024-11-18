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

#Create variables
Ax = 1.3
Ay = 1000
Bx = 5
By = 7000
Cx = 30
Cy = 1500000
Dx = 120
Dy = 25000
Ex = 1200
Ey = 1500000

#Calculate slope function
def calcSlope (y0, y1, x0, x1):
    slope = (log10(y1/y0))/(log10(x1/x0))
    return slope

#Take input of the excess temperature
num = float(input("Enter the excess temperature:"))
#Separate the graph into four different sections based on the points
if num < Ax:
    print("Surface heat flux is not available")
elif Ax <= num < Bx:
    output = Ay*((num/Ax)**calcSlope(Ay, By, Ax, Bx))
    output = round(output)
    print(f"The surface heat flux is approximately {output} W/m^2")
elif Bx <= num < Cx:
    output = By*((num/Bx)**calcSlope(By, Cy, Bx, Cx))
    output = round(output)
    print(f"The surface heat flux is approximately {output} W/m^2")
elif Cx <= num < Dx:
    output = Cy*((num/Cx)**calcSlope(Cy, Dy, Cx, Dx))
    output = round(output)
    print(f"The surface heat flux is approximately {output} W/m^2")
elif Dx <= num <= Ex:
    output = Dy*((num/Dx)**calcSlope(Dy, Ey, Dx, Ex))
    output = round(output)
    print(f"The surface heat flux is approximately {output} W/m^2")
elif num > Ex:
    print("Surface heat flux is not available")
