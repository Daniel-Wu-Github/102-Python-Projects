# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 1.11
# Date: 24th August 2023
#
#
# YOUR CODE HERE
#
import math

x1 = 10.0
x2 = 55.0
y1 = 2027.0
y2 = 23027.0
x0 = 25.0

slope1 = (y2-y1)/(x2-x1)

part1 = slope1*(x0-x1)+y1

print("for t = 25 minutes, the position p",part1,"kilometers")

earthR = 6745.0
earthD = 2*earthR*math.pi
x3 = 300.0

part2 = slope1*(x3-x1)+y1

while part2 >= earthD:
    part2 -= earthD
    
print("For t = 300 minutes, the position p =",part2,"kilometers")
    
#comments to future self