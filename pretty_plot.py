import numpy as np
import matplotlib.pyplot as plt

point = np.array([0, 1])


matrix = np.array([[1.02, 0.095], [-0.095, 1.02]])


points = []


for _ in range(250):
    point = np.matmul(matrix, point)
    points.append(point)
    print("This point is now",point)


x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]


plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='red')
plt.xlabel('X-Coordinates')
plt.ylabel('Y-Coordinates')
plt.title('Trajectory of Points - Archimedes Spiral')

plt.show()
