import numpy as np
import matplotlib.pyplot as plt

#used defined variables
x = np.random.random_sample((7,)) # X coordinate control points
y = np.random.random_sample((7,)) # Y coordinate conrol points
z = np.random.random_sample((7,)) # Z coordinate control points

cells = 100 # total number of divisions for Bezier curve

# Other Variables
nCPTS = np.size(x, 0) # Total Number of Control Points
n = nCPTS - 1 # Total Number of Segments
i = 0 # Control Point Counter
t = np.linspace (0,1, cells) # Parametric Variable
b = [] # Initialized Empty Matrix for Bernstein Basis Polynomial

# Initialized Empty Matrix for X, Y, and Z, Bezier Curve
xBezier = np.zeros((1, cells)) 
yBezier = np.zeros((1, cells)) 
zBezier = np.zeros((1, cells))

#Binomial coefficients
def Ni(n, i): 
    return np.math.factorial(n) /(np.math.factorial(i) * np.math.factorial (n - i))

#Berstain basis function
def basisfunction(n,i,t):
    J = np.array(Ni(n, i)* (t ** i) * (1 - t) ** (n - i)) 
    return J

for k in range(0,nCPTS):
    b.append(basisfunction(n,i,t))

    xBezier = basisfunction(n,i,t) * x[k] + xBezier
    yBezier = basisfunction(n,i,t) * y[k] + yBezier
    zBezier = basisfunction(n,i,t) * z[k] + zBezier
    i += 1

#plot 2d graph
for line in b:
    plt.plot(t,line)
plt.show()

#plot 3d graph
fig1 = plt.figure(figsize =(4,4))
ax1=fig1.add_subplot(111,projection='3d')
ax1.scatter(x,y,z,c='black')
ax1.plot(xBezier[0],yBezier[0],zBezier[0],c='blue')
plt.show()
