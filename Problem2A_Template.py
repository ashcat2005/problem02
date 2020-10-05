'''
Computational Astrophysics 
2020

Problem 02
Boundary Value Problem (BVP) Template
Shooting Algorithm
'''
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Set up the grid
rmin = 0.0
rmax = [INSERT HERE] # Value of the radius of the star R
n = 10000 # You can change the number of points 
r = np.linspace(rmin,rmax,n)
h = x[1]-x[0]

# Boundary conditions
A = 0.0 # inner boundary
B = [INSERT HERE] # outer boundary


rho = [INSERT HERE] # Read the density function obtained in Problem 01


def ODE(r0, q0):
    f = np.zeros(2)
    f[0] = [INSERT HERE]
    f[1] = [INSERT HERE]

    return f

def FEuler(h, t0, q0):
    '''
    ------------------------------------------
    FEuler(h, t0, q0)
    ------------------------------------------
    Forward Euler's method for solving a ODEs 
    system.
    Arguments:
    h: stepsize for the iteration
    t0: independent parameter initial value
    q0: numpy array with the initial values of
        the functions in the ODEs system
    ------------------------------------------
    '''
    f = ODE(t0, q0)
    q1 = q0 + h*f
    return q1

# Give initial guess for the derivative
z0 = [INSERT HERE] 
z1 = [INSERT HERE]

i = 0
imax = 100 # Maximum number of steps in the root finding algorithm


# Shooting Method
# Main loop for solving the problem including the secant method
while (np.abs(Phi_0)>1E-10 and i<imax):
    [INSERT HERE]



# Plot the solution
[INSERT HERE] 




