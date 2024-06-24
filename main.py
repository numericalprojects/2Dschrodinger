# Program: schrodinger
# By: Nathan Crawford
#-----------------------------------------------------------------------------
# This program solves the 2D Time Independent Schrodinger Equation with the 
# ARPACK by first taking input from the user, initializing the 
# 2D grid, constructing the Hamiltonian matrix and solving the eigenvalue 
# problem and plotting the potentials and probability densities. 
#-----------------------------------------------------------------------------
from inputoutput import read_input, plot_potential, plot_densities 
from linearalgebra import creategrid, eigen_solve 
from quantum import create_potential, create_kinetic, create_hamiltonian

# Take input from the user. TODO: maybe make a namelist instead? 
potential_inp, states, L, N  = read_input() 

print("input read ") #Print statements to track progress of the program. 

#Create a 2 dimensional grid 
x, y = creategrid(L, N) 
 
print("xy grid created")

#Create the potential energy matrix. Note that since 0s are everywhere, it's really just an array. 
#Refer to the README for clarification on how the operators are constructed. 
potential = create_potential(x, y, L, potential_inp) 

print("potential made") 

#Create the kinetic energy matrix. 
kinetic = create_kinetic(N) 

print("kinetic made")

#Create the Hamiltonian. This is easy because we're just adding the potential energy and kinetic energy operators. 
hamiltonian = create_hamiltonian(potential, kinetic, N) 
print("H made")

#Solve system. e_values are the eigenvalues and e_vec are the eigenvectors. 
#Note for a hydrogen like potential my machine(which isn't very good) had some trouble. 
e_values, e_vec = eigen_solve(hamiltonian, states) 
print("system solved")

#We can really do this part earlier but we should have some idea of what potentials should look like already. 
#This is mainly to make sure everything is setup right prior to solving the system. 
plot_potential(potential, x, y)
print("potential plotted")

#Now the important results. When solving these systems, the probability densities and the eigenvalues are the 
#main results of interest. TODO: find a way to represent the eigenvalues on a graph. 
plot_densities(e_vec, x, y, states, N)