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
''' Enter the side length in meters: 1
Enter the number of layers: 5
You need 55.83 m^2 of gold foil to cover the pyramid'''
from math import *
side = float(input("Enter the side length in meters:"))
layers = int(input("Enter the number of layers:"))

a = 0
for i in range (1, layers+1):
    h = side
    l = i*side
    old = side*(i-1)
    
    a+= (sqrt(3))*((l**2)/4) + (3*l*h)
    a-= (sqrt(3))*((old**2)/4)

print (f"You need {(a):.2f} m^2 of gold foil to cover the pyramid")
#comment