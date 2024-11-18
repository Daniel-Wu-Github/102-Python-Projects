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
#Calculate the force in Newtons applied to an object with mass 27 kg and acceleration 1.5 m/s^2. According to Newton’s Second Law the net force applied to an object produces a proportional acceleration.
#Calculate the wavelength of x-rays scattering from a crystal lattice with a distance between crystal layers of 0.025 nm, scattering angle of 35 degrees, and first order diffraction. Bragg’s Law describes the scattering of waves from a crystal using the equation nλ = 2d sin θ The standard unit of wavelength in the SI system is nanometers (nm).
#Calculate how much Radon-222 is left after 5 days of radioactive decay given an initial amount of 27 g and a half-life of 3.8 days. The equation for radioactive decay is N(t) = N02^(−t/t_half) where N0 is the intial amount (units of grams), t is the time (units of days), and t_half is the half-life (units of days).
#Calculate the pressure of 5 moles of an ideal gas with a volume of 0.27 m^3, and temperature of 415 K. The Ideal Gas Law is the equation of state of a hypothetical ideal gas and is a good approximation of the behavior of gases under many conditions. Use a value of 8.314 m^3Pa/K·mol for the gas constant. The standard unit of pressure in the SI system is kilopascals (kPa). Hint: convert the units at the end of your calculation
import math

object1 = 27.0
force1 = 1.5
acceleration = object1*force1
print("Force is",acceleration,"N")


wL = 0.025
wL*=2
rad1 = 35
rad1 = rad1*(math.pi/180)
wL*=math.sin(rad1)
print("Wavelength is",wL,"nm")

radon3 = 27
ratio1 = 5/3.8
halfLife = math.pow(0.5, ratio1)
radon3 *= halfLife
print("Radon-222 left is",radon3,"g")

volume = 0.27
nMoles = 5
temperature = 415
idealK = 8.314
pressure = (nMoles*temperature*idealK)/volume
pressure /= 1000

print("Pressure is",pressure,"kPa")
