# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
import numpy as np

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)

print("A =",end=" ")
print(A)
print()

print("B =",end=" ")
print(B)
print()

print("C =",end=" ")
print(C)
print()

D = np.dot(np.dot(A, B), C)

print("D =",end=" ")
print(D)
print()

print("D^T =",end=" ")
print(D.T)
print()

E = np.sqrt(D) / 2
print("E =",end=" ")
print(E)
