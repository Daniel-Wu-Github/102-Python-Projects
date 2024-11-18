# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
# Names: Gabriel Deem
# Andrew Wu
# Daniel Wu
# Ricky Alviso
# Section: 564
# Assignment: 
# Date: 12/9/2023
from math import * 

############ Part A ############
a = str(input("Enter True or False for a: "))
b = str(input("Enter True or False for b: "))
c = str(input("Enter True or False for c: "))
if(a == "True" or a == "T" or a =="t"):
    a = True
else:
    a = False

if(b == "True" or b == "T" or b =="t"):
    b = True
else:
    b= False
    
if(c == "True" or c == "T" or c =="t"):
    c = True
else:
    c = False

############ Part B ############
AnBnC = (a and b and c)
AoBoC = (a or b or c)
print("a and b and c: ",AnBnC)
print("a or b or c: ", AoBoC)

############ Part C ############
AorB = (a or b) #comment
AnB = (a and b)
XOR = (AorB != AnB)
print("XOR: ",XOR)

c2 = (XOR != c) or (a and b and c)

print ("Odd number:",c2)

############ Part D ############
#(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
#(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))

comp1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
comp2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
simp1 = (not(a or b)) or ((b and not(a or c)) or (a and (not b)))
simp2 = ((not(b or not c)) or (a and c)) or ((not c) and (b and c)) or (a and not c)
print("Complex 1:",comp1)
print("Complex 2:",comp2)
print("Simple 1:",simp1)
print("Simple 2:",simp2)



