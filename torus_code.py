import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Defining the number of points
n = 100

# Creating the angles theta and phi
theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)

# Radius from the center of the torus tube to the center of the torus (R) and tube radius (r)
R, r = 2, 1

# Parametric equations of the torus
x = (R + r*np.cos(theta)) * np.cos(phi)
y = (R + r*np.cos(theta)) * np.sin(phi)
z = r * np.sin(theta)

# Creating the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the surface of the torus
ax.plot_surface(x, y, z, color='b', edgecolors='w')

# Setting the z-axis limits
ax.set_zlim(-3, 3)

# Displaying the graph
plt.show()
