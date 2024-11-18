# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
import numpy as np
import matplotlib.pyplot as plt

# Plotting two parabolas for different focal lengths
x = np.linspace(-2.0, 2.0, 100)
y1 = 1 / (4 * 2) * x**2  # Parabola with focal length f = 2
y2 = 1 / (4 * 6) * x**2  # Parabola with focal length f = 6

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='f = 2', linewidth=2.0, color='blue')
plt.plot(x, y2, label='f = 6', linewidth=6.0, color='orange')
plt.title('Parabolas with Different Focal Lengths')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Plotting points for the cubic polynomial
x_cubic = np.linspace(-4.0, 4.0, 25)
y_cubic = 2 * x_cubic**3 + 3 * x_cubic**2 - 11 * x_cubic - 6

plt.figure(figsize=(8, 6))
plt.scatter(x_cubic, y_cubic, color='green', label='Cubic Polynomial')
plt.title('Cubic Polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Plotting sin(x) and cos(x) in two subplots
x_sin_cos = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_sin = np.sin(x_sin_cos)
y_cos = np.cos(x_sin_cos)

plt.figure(figsize=(10, 6))

# Subplot 1: sin(x)
plt.subplot(2, 1, 1)
plt.plot(x_sin_cos, y_sin, color='blue', label='sin(x)')
plt.title('sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()

# Subplot 2: cos(x)
plt.subplot(2, 1, 2)
plt.plot(x_sin_cos, y_cos, color='red', label='cos(x)')
plt.title('cos(x)')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.legend()

plt.tight_layout()
plt.show()
