import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, interp1d

# Parametric Lagrange Interpolation (2D)
def parametric_lagrange_interpolation_2d(t, x, y, num_points):
    t_new = np.linspace(t.min(), t.max(), num_points)
    x_interp = lagrange(t, x)(t_new)
    y_interp = lagrange(t, y)(t_new)
    return x_interp, y_interp

# Parametric Hermite Interpolation (2D)
def parametric_hermite_interpolation_2d(t, x, y, num_points):
    t_new = np.linspace(t.min(), t.max(), num_points)
    x_interp = interp1d(t, x, kind='cubic')(t_new)
    y_interp = interp1d(t, y, kind='cubic')(t_new)
    return x_interp, y_interp

# Parametric Cubic Interpolation (3D)
def parametric_cubic_interpolation_3d(t, x, y, z, num_points):
    t_new = np.linspace(t.min(), t.max(), num_points)
    x_interp = interp1d(t, x, kind='cubic')(t_new)
    y_interp = interp1d(t, y, kind='cubic')(t_new)
    z_interp = interp1d(t, z, kind='cubic')(t_new)
    return x_interp, y_interp, z_interp

# Generate sample data
t = np.array([0, 1, 2, 3, 4])
x = np.array([1, 2, 0, 3, 2])
y = np.array([3, 1, 4, 2, 0])
z = np.array([2, 1, 3, 0, 4])

# Interpolate data
num_points = 100
x_lagrange, y_lagrange = parametric_lagrange_interpolation_2d(t, x, y, num_points)
x_hermite, y_hermite = parametric_hermite_interpolation_2d(t, x, y, num_points)
x_cubic, y_cubic, z_cubic = parametric_cubic_interpolation_3d(t, x, y, z, num_points)

# Plot results
plt.figure(figsize=(12, 5))

# 2D Plots
plt.subplot(121)
plt.plot(x_lagrange, y_lagrange, label='Lagrange Interpolation')
plt.plot(x_hermite, y_hermite, label='Hermite Interpolation')
plt.plot(x, y, 'ro', label='Original Points')
plt.legend()
plt.title('Parametric Lagrange and Hermite Interpolation (2D)')

# 3D Plot
ax = plt.subplot(122, projection='3d')
ax.plot(x_cubic, y_cubic, z_cubic, label='Cubic Interpolation')
ax.scatter(x, y, z, color='r', label='Original Points')
ax.legend()
ax.set_title('Parametric Cubic Interpolation (3D)')

plt.show()
