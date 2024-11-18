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
side = float(input("Enter the side length in meters:"))
layer = int(input("Enter the number of layers:"))
area = (layer/2)*(((sqrt(3) / 4) * side ** 2)+((sqrt(3) / 4) * side ** 2) + ((layer - 1) * ((2*(side)** 2)*(sqrt(3)/4))))
area+= (layer/2)*((3 * side * side)+(3 * side * side) + (layer-1)*(3*side*side))
#comment
   
print(f"You need {area:0.2f} m^2 of gold foil to cover the pyramid")
