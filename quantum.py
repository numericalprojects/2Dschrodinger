#-----------------------------------------------------------------------
#Module: quantum
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## This is the physics module. All functions here are related to our specific 
## physical system at hand. 
##---------------------------------------------------------------------- 
##
## Included functions:
## create_potential
## oscillator 
## inf_well
## gaussian 
## hydrogen
## create_kinetic
## create_hamiltonian 
##
#----------------------------------------------------------------------- 

import numpy as np 
from linearalgebra import create_2d_lap 
from scipy import sparse 

#-----------------------------------------------------------------------
## Function: create potential 
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Creates the potential energy matrix based off which potential the user 
## selected. 
##----------------------------------------------------------------------
## Input:
## x                points from -L to L on x axis
## y                points from -L to L on y axis
## L                length of the potential 
## potential_inp    character representing the user input for which potential to use.
##----------------------------------------------------------------------
## Output: 
## potential        potential energy matrix   
##----------------------------------------------------------------------
def create_potential(x, y, L, potential_inp):

    # Create potential energy matrix based off what the user inputted
    
    if(potential_inp == 'O'):
        potential = oscillator(x, y) 
    elif(potential_inp == 'I'): 
        potential = inf_well(x, y) 
    elif(potential_inp == 'G'): 
        potential = gaussian(x, y, L) 
    elif(potential_inp == 'H'): 
        potential = hydrogen(x, y) 
    
    # Realistically the program shouldn't get here due to the checks in read_input but 
    # this is a decent failsafe just in case.
    else: 
        print(" \n No potential input detected. Exiting program. \n") 
        quit()
    return potential

#-----------------------------------------------------------------------
## Function: oscillator
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Creates harmonic oscillator potential  
##----------------------------------------------------------------------
## Input:
## x                points from -L to L on x axis
## y                points from -L to L on y axis
##----------------------------------------------------------------------
## Output: 
## v                potential energy matrix   
##----------------------------------------------------------------------
def oscillator(x, y):
    v = (x**2 + y**2)/2
    return v 

#-----------------------------------------------------------------------
## Function: inf_well
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Creates particle in a box potential  
##----------------------------------------------------------------------
## Input:
## x                points from -L to L on x axis
## y                points from -L to L on y axis
##----------------------------------------------------------------------
## Output: 
## v                potential energy matrix   
##----------------------------------------------------------------------
def inf_well(x, y): 
    v = 0 * x * y 
    return v 

#-----------------------------------------------------------------------
## Function: gaussian
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Creates gaussian potential  
##----------------------------------------------------------------------
## Input:
## x                points from -L to L on x axis
## y                points from -L to L on y axis 
## L                length and width of potential grid
##----------------------------------------------------------------------
## Output: 
## v                potential energy matrix   
##----------------------------------------------------------------------
def gaussian(x, y, L): 
    v = np.exp(-0.5*((x/L)**2 + (y/L)**2)/(0.2**2)) 
    return v  

#-----------------------------------------------------------------------
## Function: hydrogen
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Creates hydrogen like potential  
##----------------------------------------------------------------------
## Input:
## x                points from -L to L on x axis
## y                points from -L to L on y axis
##----------------------------------------------------------------------
## Output: 
## v                potential energy matrix   
##----------------------------------------------------------------------
def hydrogen(x, y): 
    
    # Shift slightly to account for divergence issue.  
    v = -1/(np.sqrt(x**2 + y**2) + 0.0002) 
    return v 

#-----------------------------------------------------------------------
## Function: create_kinetic
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Creates kinetic energy operator matrix. Refer to README on how this is 
## defined. 
##----------------------------------------------------------------------
## Input:
## N                discretized points from -L to L. 
##----------------------------------------------------------------------
## Output: 
## T                kinetic energy matrix   
##----------------------------------------------------------------------
def create_kinetic(N): 
    T = create_2d_lap(N) 
    T = -1/2 * T 
    return T 

#-----------------------------------------------------------------------
## Function: create_hamiltonian
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Creates hamiltonian operator matrix  
##----------------------------------------------------------------------
## Input:
## potential                points from -L to L on x axis
## kinetic                  points from -L to L on y axis 
## N                        
##----------------------------------------------------------------------
## Output: 
## v                        discretized points from -L to L.  
##----------------------------------------------------------------------
def create_hamiltonian(potential, kinetic, N): 
    
    # v right now is an NxN grid but if you recall how we defined the problem in the 
    # README, the potential energy matrix is really just N**2 entries on the diagonal. 
    # Therefore, we reshape it before adding it to the kinetic energy. 

    v = sparse.diags(potential.reshape(N**2), (0)) 
    H = kinetic + v 
    return H 