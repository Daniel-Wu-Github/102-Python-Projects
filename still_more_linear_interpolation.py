# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Gabriel Deem
# Daniel Wu
# Erica Yi
# Madelynn Johnson
# Section: 564
# Assignment: Lab 3.15
# Date: 31/8/2023
t1 = float(input("Enter time 1:"))
x1 = float(input("Enter the x position of the object at time 1:"))
y1 = float(input("Enter the y position of the object at time 1:"))
z1 = float(input("Enter the z position of the object at time 1:"))
t2 = float(input("Enter time 2:"))
x2 = float(input("Enter the x position of the object at time 2:"))
y2 = float(input("Enter the y position of the object at time 2:"))
z2 = float(input("Enter the z position of the object at time 2:"))

startingTime = t1
endingTime = t2
interval = (t2-t1)/4


while startingTime <= endingTime:
    slope1 = (x2-x1)/(t2-t1)
    partX = slope1*(startingTime-t1)+x1

    slope2 = (y2-y1)/(t2-t1)
    partY = slope2*(startingTime-t1)+y1

    slope3 = (z2-z1)/(t2-t1)
    partZ = slope3*(startingTime-t1)+z1
    print(f"At time {startingTime:.2f} seconds the object is at ({partX:.3f}, {partY:.3f}, {partZ:.3f})")
    startingTime+=interval
    
    
    
#comments to future self
