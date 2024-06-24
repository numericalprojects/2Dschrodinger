#-----------------------------------------------------------------------
#Module: inputoutput
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## This is the module that reads input from the user at the beginning and 
## outputs at the end
##---------------------------------------------------------------------- 
##
## Included functions:
## read_input
## check_input_pot 
## check_inp_pos_int
## check_inp_pos_real
## plot_potential 
## plot_densities 
## reshape_evec
##
#----------------------------------------------------------------------- 

import matplotlib.pyplot as plt 

def read_input(): 
    
        print("Greetings user. This program solves the 2D Time Independent Schrodinger Equation. \n") 
    
        print("Please Select potential. Refer to README for different potential functions. \n") 
    
        print("Type O for Harmonic Oscillator, I for Infinite Square Well, G for Gaussian Well or H for Hydrogen Atom. \n") 
    
        print("Or type S to stop the program \n") 

        # Here we have a series of input checks in case the user doesn't enter something 
        # valid. 
        try:
            potential = check_input_pot()
        except ValueError as e:
            print(e) 


        print("\n Enter input integer for number of states to solve for. \n") 
        states = check_inp_pos_int() 
        
        

        print("\n Enter a real number input for length and height of the XY grid L \n") 
        L = check_inp_pos_real() 

        print("\n Enter integer input for number of discretized steps between -L and L \n") 
        N = check_inp_pos_int()  

        
        return potential, states, L, N  

#-----------------------------------------------------------------------
## Function: check_input_pot
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Checks input for potential. 
##----------------------------------------------------------------------
## Input:
## N/A
##----------------------------------------------------------------------
## Output: 
## pot_inp          user input for potential energy    
##----------------------------------------------------------------------
def check_input_pot():
    
    # Options are the potentials or to stop the program. 
    allowed_characters = {'O', 'I', 'G', 'H', 'S'}
    
    pot_inp = input() 

    #If input is incorrect then just exit, otherwise return it. 
    if pot_inp in allowed_characters and len(pot_inp) == 1:
        if pot_inp == 'S': 
            SystemExit 
        else: 
            return pot_inp 
    else:
        raise ValueError("Invalid input. Please enter exactly one character from the set {O, I, G, H or S}.") 
        
#-----------------------------------------------------------------------
## Function: check_input_pos_int
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Checks input to make sure it is a positive integer.  
##----------------------------------------------------------------------
## Input:
## N/A
##----------------------------------------------------------------------
## Output: 
## user_inp          user input   
##----------------------------------------------------------------------
def check_inp_pos_int(): 
    
    # This is for number of states and discretized steps. 
    # It should be an integer greater than zero. 
    
    user_inp = input() 

    number = int(user_inp)
    
    if number > 0:
         
        return number  
    else:
        print(" \n Input must be a positive integer. \n") 
        quit() 

#-----------------------------------------------------------------------
## Function: check_input_pos_real
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Checks input to make sure it is a positive real number. 
##----------------------------------------------------------------------
## Input:
## N/A
##----------------------------------------------------------------------
## Output: 
## user_inp          user input     
##----------------------------------------------------------------------
def check_inp_pos_real(): 

    # This is for the length of the box. 
    # Must have a positive length. 
    user_inp = input() 
    number = float(user_inp)
    
    if number > 0:
         
        return number  
    else:
        print(" \n Input must be a positive real number. \n") 
        quit()

#-----------------------------------------------------------------------
## Function: plot_potential
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Makes a contour plot of the potential energy function 
##----------------------------------------------------------------------
## Input:
## v                 potential energy matrix 
## x                 array containing x coordinates 
## y                 array containing y coordinates 
##----------------------------------------------------------------------
## Output: 
## N/A    
##----------------------------------------------------------------------
def plot_potential(v, x, y): 
    plot0 = plt.figure(0,figsize=(8,6))
    plt.contourf(x,y,v,100)
    plt.colorbar()
    plt.title("Plot of V")
    plt.xlabel(r'$X$')
    plt.ylabel(r'$Y$') 
    plt.show() 
    return 

#-----------------------------------------------------------------------
## Function: plot_densities
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Makes a contour plot of the probability densities.
##----------------------------------------------------------------------
## Input:
## e_vec             eigenvectors of the Hamiltonian
## x                 array containing x coordinates
## y                 array containing y coordinates 
## states            user inputted number of excited states 
## N                 user inputted number of discretized steps 
##----------------------------------------------------------------------
## Output: 
## N/A    
##----------------------------------------------------------------------
def plot_densities(e_vec, x, y, states, N): 
    # Loop to create a contour plot for each excited state 
    for n in range (0,states): 
        plot2 = plt.figure(2, figsize=(8,6)) 
        plt.contourf(x,y, reshape_evec(e_vec, n, N)**2,300) 
        plt.colorbar() 
        plt.title("Plot of Probability Density for the {} state".format(n)) 
        plt.xlabel(r'$X$')
        plt.ylabel(r'$Y$') 
        plt.show()
    return 

#-----------------------------------------------------------------------
## Function: plot_densities
#-----------------------------------------------------------------------
## By: Nathan Crawford
##
## Reshapes the eigenvector so it has the right shape to be plotted. 
##----------------------------------------------------------------------
## Input:
## e_vec             eigenvectors of the Hamiltonian
## n                 integer designating the specific eigenvector 
## N                 user inputted number of discretized steps 
##----------------------------------------------------------------------
## Output: 
## e_vec             reshaped eigenvector
##----------------------------------------------------------------------
def reshape_evec(e_vec, n, N): 
    # NumPy expects the e-vector to be NxN for the 2D grid. 
    # So we take the column and transpose it to make it a row 
    # and make it NxN. 
    return e_vec.T[n].reshape((N,N))
