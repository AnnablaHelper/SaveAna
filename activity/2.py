import numpy as np
import matplotlib.pyplot as plt

def compute_cubic_bezier(n, points, guidepoints):
    coefficients = []
    for i in range(n):
        xi, yi = points[i]
        x_plus_i, y_plus_i = guidepoints[i]
        xi_plus_1, yi_plus_1 = points[i+1]
        x_minus_i_plus_1, y_minus_i_plus_1 = guidepoints[i+1]
        
        a0 = xi
        b0 = yi
        a1 = 3 * (x_plus_i - xi)
        b1 = 3 * (y_plus_i - yi)
        a2 = 3 * (xi + x_minus_i_plus_1 - 2 * x_plus_i)
        b2 = 3 * (yi + y_minus_i_plus_1 - 2 * y_plus_i)
        a3 = xi_plus_1 - xi + 3 * (x_plus_i - x_minus_i_plus_1)
        b3 = yi_plus_1 - yi + 3 * (y_plus_i - y_minus_i_plus_1)
        
        coefficients.append((a0, a1, a2, a3, b0, b1, b2, b3))
    
    return coefficients

def plot_cubic_bezier(coefficients):
    t = np.linspace(0, 1, 100)
    for coeff in coefficients:
        a0, a1, a2, a3, b0, b1, b2, b3 = coeff
        x = a0 + a1 * t + a2 * t**2 + a3 * t**3
        y = b0 + b1 * t + b2 * t**2 + b3 * t**3
        plt.plot(x, y)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cubic Bézier Curves')
    plt.grid(True)
    plt.show()

# Example usage
n = 1
points = [(0, 0), (1, 2), (3, -1), (4, 0)]
guidepoints = [(1, 1), (2, 3), (2, -2), (3, 1)]



coefficients = compute_cubic_bezier(n, points, guidepoints)
plot_cubic_bezier(coefficients)
