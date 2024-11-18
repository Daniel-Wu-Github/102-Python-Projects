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

x1 = 8
x2 = -5
y1 = 6
y2 = 30
z1 = 7
z2 = 9
t1 = 12
t2 = 85
t0 = 30



startingTime = 30.0
endingTime = 60.0

while startingTime <= endingTime:
    slope1 = (x2-x1)/(t2-t1)
    partX = slope1*(startingTime-t1)+x1

    slope2 = (y2-y1)/(t2-t1)
    partY = slope2*(startingTime-t1)+y1

    slope3 = (z2-z1)/(t2-t1)
    partZ = slope3*(startingTime-t1)+z1
    print("At time",startingTime,"seconds:")
    print("x1 =",partX,"m")
    print("y1 =",partY,"m")
    print("z1 =",partZ,"m")
    print("---------------------------")
    startingTime+=7.5
    
    
    
#comments to future self