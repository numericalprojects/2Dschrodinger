# 2D Schrodinger Equation 
## Goal of the Program 
 The goal of this program is to find numerical solutions to the eigenvalue problem, the time-independent Schrodinger Equation. 
 We will work in 2 dimensions so the equation becomes: 
 $[\frac{-ℏ^2}{2m}\frac{d^2}{dx^2}\frac{d^2}{dy^2} + V(x,y)]Ψ(x,y) = EΨ(x,y)$ 

 This program is meant to be a personal exercise to extend what was accomplished in the repository quantum-eigenvalues 
 to 2 dimensions. 
 
 We want to solve this for different potentials $V(x,y)$. The potentials will be infinite square well, harmonic oscillator, 
 a Gaussian-like potential and a hydrogen-like potential. The infinite square well has analytical solutions as well as the harmonic 
 oscillator and even hydrogen in 3 dimensions but for a Gaussian-like potential we must use numerical solutions. 
 


### First part. Problem setup
 We know how to solve the Schrodinger equation in 1D. The problem now is to extend it to 2D. Lets first look at the eigenvectors $ψ$. 
 In 1 dimension $ψ$ looks like this: 
 
 ```math
ψ = \begin{bmatrix}ψ_{1}\\ψ_{2}\\ \vdots\\ψ_{N - 1} \end{bmatrix}
```
 ### Second part. Harmonic Oscillator 
 The next part does the same thing but with the quantum harmonic oscillator where $V(x) = \frac{ℏ^2 x^2}{2m}$. This is also a well understood problem with 
 an analytical solution(granted it's a little harder). The eigenfunctions here should look like Gaussians. We can compare the eigenvalues to the analytical 
 expression: 
 $E_i = (i- \frac{1}{2})ℏ^2/m$. The program will do the same things as before. 
 
 ### Third part. Woods Saxon 
 The last part of this program is the Woods Saxon potential $V(x)= \frac{-V_0}{1 + exp((|x|-R)/a)}$. The program will do the same thing as the previous 2, 
 but this time will also write the 3 lowest energies as a function of $R$ going from 2 to 10. 
 
 ### Jupyter Notebook 
 Once the program is finished we can head over to jupyter and there should be 4 different plots: 
 1. The ground state normalized probability density for the 3 different problems
 2.The 1st excited state normalized probability density for the 3 different problems
 3.The 2nd excited state normalized probability density for the 3 different problems
 4.The three lowest energies for the Woods-Saxon potential as a function of the radius 
 
 ### Compiling the program 
 It would be quite beneficial to you if you had a Linux system because it would enable you to use the makefile included. 
If you don't then you'll need to adjust the source code itself to solve the eigenvalue problem.

If this is the case then what you do is open a terminal, use the cd command to change to this directory. 

Then type make. 

You'll see some gfortran commands being executed. All of this has created an exectuable file called woods_saxon

Then the program will ask for input. Traps have been set in case you accidentally enter invalid input. 

Results will be displayed on screen and written into several files. Now you can head over to Jupyter Notebook 
to analyze the results. 
