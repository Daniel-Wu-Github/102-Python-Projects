# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#
#
# YOUR CODE HERE
#

import math
print("This program calculates the applied force given mass and acceleration")
print('Please enter the mass (kg):', end=' ')
object1 = float(input())
print('Please enter the acceleration (m/s^2):', end=' ')
acceleration = float(input())
force = object1*acceleration
force = round(force,1)
print('Force is',force,'N')

print("This program calculates the wavelength given distance and angle")
print('Please enter the distance (nm):', end=' ')
wL = float(input())
wL*=2
print('Please enter the angle (degrees):', end=' ')
rad1 = float(input())
rad1 = rad1*(math.pi/180)
wL*=math.sin(rad1)
#wL = round(wL,4)
print(f"Wavelength is {wL:.4f} nm")

print("This program calculates how much Radon-222 is left given time and initial amount")
print('Please enter the time (days):', end=' ')
ratio1 = float(input())/3.8
print('Please enter the initial amount (g):', end=' ')
radon3 = float(input())
halfLife = math.pow(0.5, ratio1)
radon3 *= halfLife
radon3 = round(radon3,2)
print("Radon-222 left is",radon3,"g")

print("This program calculates the pressure given moles, volume, and temperature")
print("Please enter the number of moles: ", end=' ')
nMoles = float(input())
print("Please enter the volume (m^3): ", end=' ')
volume = float(input())
print("Please enter the temperature (K):", end=' ')
temperature = float(input())
idealK = 8.314
pressure = (nMoles*temperature*idealK)/volume
pressure /= 1000
pressure = round(pressure)
print("Pressure is",pressure,"kPa")


#comment
