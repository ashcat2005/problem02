'''
Computational Astrophysics 
2020

Problem 02
Boundary Value Problem (BVP) Template
Finite Differences Method
'''
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


# Set up the grid
rmin = 0.0
rmax = [INSERT HERE] # Value of the radius of the star R obtained in Problem01
N = 10000 # You can change the number of points 
n = N-1
r = np.linspace(rmin,rmax,n)
h = x[1]-x[0]

# Boundary conditions
A = 0.0 # inner boundary
B = [INSERT HERE] # outer boundary


rho = [INSERT HERE] # Read the density function obtained in Problem 01


# Here you define the size of the LSE
A = np.zeros([n,n]) 
b = np.zeros(n)

# Definition of the matrix A
[INSERT HERE]

# Definition of the vector B
[INSERT HERE]

# Forward Elimination
d = np.zeros(n)
y = np.zeros(n)

d[1] = A[1,1]
y[1] = b[1]/d[1]

[INSERT HERE]


# Backward Elimination
phi = np.zeros(N)
phi[0] = A
phi[N-1] = B

[INSERT HERE]


# Plot the solution
[INSERT HERE] 




