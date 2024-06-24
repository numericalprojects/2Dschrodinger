#-----------------------------------------------------------------------
#Module: linear algebra
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## This is the math module. These functions act independently and work regardless 
## of the physical system we are dealing with. 
##---------------------------------------------------------------------- 
##
## Included functions:
## creategrid
## create_2d_lap 
## eigen_solve
##
#----------------------------------------------------------------------- 

import numpy as np 
from scipy import sparse 
from scipy.sparse.linalg import eigsh 
from scipy.sparse.linalg import eigs

#-----------------------------------------------------------------------
## Function: creategrid
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Creates kinetic energy operator matrix. Refer to README on how this is 
## defined. 
##----------------------------------------------------------------------
## Input: 
## L                length and width of 2d grid. 
## N                discretized points from -L to L. 
##----------------------------------------------------------------------
## Output: 
## x                array containing points on x axis
## y                array containing points on y axis   
##----------------------------------------------------------------------
def creategrid(L, N): 
    x_pts = np.linspace(-L, L, N, dtype = float) 
    y_pts = np.linspace(-L, L, N, dtype = float) 
    x, y = np.meshgrid(x_pts, y_pts) 
    return x, y 

#-----------------------------------------------------------------------
## Function: create_2d_lap
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Creates the 2D laplacian as defined in the README.  
##----------------------------------------------------------------------
## Input: 
## N                discretized points from -L to L. 
##----------------------------------------------------------------------
## Output: 
## lap              2D laplacian  
##----------------------------------------------------------------------
def create_2d_lap(N): 
    # Use an array of ones to create the diagonals of D. 
    one = np.ones([N])
    diags = np.array([one, -2*one, one]) 
    # spdiags conveniently lets us create a sparse matrix and lets us place the diagonals. 
    D = sparse.spdiags(diags, np.array([-1,0,1]), N, N) 

    # This sum creates an N**2 x N**2 matrix. Even for simple systems this is computationally 
    # expensive to solve.
    lap = sparse.kronsum(D,D)
    return lap  

#-----------------------------------------------------------------------
## Function: eigen_solve
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Finds eigenvalues and eigenvectors of a matrix.   
##----------------------------------------------------------------------
## Input: 
## hamiltonian      matrix to find e-values and e-vectors for
## states           number of e-values and e-vectors
##----------------------------------------------------------------------
## Output: 
## e_vec            eigenvectors 
## e_values         eigenvalues   
##----------------------------------------------------------------------
def eigen_solve(hamiltonian, states): 

    # eigsh is the e-vector/e-value solver from ARPACK which is a linear algebra 
    # package written in FORTRAN77. It returns k eigenvectors and k eigenvalues. 
    # 'which' is a string input. SM means smallest because I want them from smallest to largest. 
    # Note this is likely to create degenerate eigenvalues. 
    
    e_vec, e_values = eigsh(hamiltonian, k= states , which='SM')
    return e_vec, e_values 