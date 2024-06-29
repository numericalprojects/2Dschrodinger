# 2D Schrodinger Equation 
## Goal of the Program 
 The goal of this program is to find numerical solutions to the eigenvalue problem, the time-independent Schrodinger Equation. 
 We will work in 2 dimensions so the equation becomes: 
 $[\frac{-ℏ^2}{2m}\frac{d^2}{dx^2}\frac{d^2}{dy^2} + V(x,y)]Ψ(x,y) = EΨ(x,y)$ 

 This program is meant to be a personal exercise to extend what was accomplished in the repository quantum-eigenvalues 
 to 2 dimensions. 
 
 We want to solve this for different potentials $V(x,y)$. The potentials will be infinite square well, harmonic oscillator, 
 a Gaussian-like potential and a hydrogen-like potential. The infinite square well has analytical solutions as well as the harmonic 
 oscillator and even hydrogen in 3 dimensions but for a Gaussian-like potential we must use numerical solutions. The wavefunction is 
 discretized on a grid from -L to L. 
 


### Hamiltonian setup
 We know how to solve the Schrodinger equation in 1D. The problem now is to extend it to 2D. Lets first look at the eigenvectors $ψ$. 
 In 1 dimension $ψ$ looks like this: 
 
 ```math
ψ = \begin{bmatrix}ψ_{1}\\ψ_{2}\\ \vdots\\ψ_{N - 1} \end{bmatrix}
```

In 2D it feels natural to turn $ψ$ into a 2D grid. 
```math
\begin{equation}
ψ =
\begin{pmatrix}
  ψ_{11}       & ψ_{12}   & \cdots  & ψ_{1N}  \\
  ψ_{21}       & ψ_{22}   & \cdots  & ψ_{2N}  \\
  \vdots  & \vdots  & \vdots  & \ddots  & \vdots \\
  ψ_{N1}       & ψ_{N2}   & \cdots  & ψ_{NN} \\
\end{pmatrix}
\end{equation}
```
However, 

When we run it through SciPy, it'll return the eigenvectors like this: 

 ```math
ψ = \begin{bmatrix}ψ_{11}\\\vdots \\ ψ_{1N}\\ψ_{21}\\\vdots\\ψ_{2N}\\\vdots\\ψ_{NN} \end{bmatrix}
```
Here you can see that it is a column vector $N^2$ long. So it will have to be converted into a 2D grid to visualize it later. 

Now the next part is to deal with the 2D Laplacian. We saw the 1D case with the tridiagonal matrix. The matrix will look similar 
here except now we can set $\hbar$ = $1$ and write units in terms of $m\Delta x^2$. This will make constructing our laplacian look 
a lot cleaner. When it comes to multi-dimensional Laplacians we use the Kroncker sum of discrete laplacians. Let's define $N$ x $N$ matrix D as 

```math
\begin{equation}
D =
\begin{pmatrix}
  -2       & 1   & 0 & \cdots  & \cdots & 0  \\
   1       & -2   & 1 & \cdots & \cdots & \vdots  \\
   0  & 1  & -2  & 1  & \cdots & \vdots \\
   \vdots       & \vdots   & \vdots  & \ddots & \cdots & 0 \\
   \vdots  & \vdots & \vdots & \ddots & \cdots & 1\\
   0 & \cdots & \cdots & 0 & 1 & -2 \\
\end{pmatrix}
\end{equation} 
```
Here we can see that the off diagonals contain 1 and the main diagonal contains -2. This comes from the 3 point approximation 
for the derivative. 

The Kroncker Sum of discrete Laplacians in 2D is $L = D_{xx} ⊕ D_{yy}$

This is computed using the Kronecker product(although SciPy performs the calculations for us): 

$D_{xx} ⊕ D_{yy} = D_{xx}⊗I + I⊗D_{yy}$ where $I$ is the identity matrix. 

This results in an $N^2$ x $N^2$ matrix and represents the kinetic energy operator. 

Recall that the potential energy was a matrix with only entries on the diagonal and 0s everywhere else. 
It will be the same here except there will be $N^2$ entries because we are in 2D. Next we add it to the kinetic energy operator and we have our hamiltonian. 

The Schrodinger Equation then becomes this 
$[\frac{-1}{2} D_{xx} ⊕ D_{yy} + m \Delta x^2]Ψ(x) =  m \Delta x^2 EΨ(x,y)$

 ### Potential Energy Setup 
 There are different potentials the user can run the program for. 
 
 First is the Infinite Square Well or Particle in a box: $V = 0$ 
 
 Next is the Harmonic Oscillator: $V(x, y) = \frac {1}{2} (x^2 + y^2)$ 

 Next is the Hydrogen-like potential: $V(r) = \frac{-1}{r}$ 
 where $r = \sqrt{x^2 + y^2}$. We will need to shift this by a small amount to 
 avoid the divergence issue so really in the code we have $V(r) = \frac{-1}{r + ϵ}$ 


 Next is the Gaussian-like potential: 
 $V(x, y) = e^(-\frac{\frac{x^2}{L^2} + \frac{y^2}{L^2}}{0.2^2})$ 
 
 
 ### User Input
 When the program runs, it will ask you to input different quantities. The first one is which potential to run it for. 
 I = Infinite square well, O = Harmonic Oscillator, H = Hydrogen-like potential, G = Gaussian-like potential. 

 The next is the number of states to run it for. Note that the ground state is calculated so if you enter 3, it will calculate 
 states 0-2. 

 Next is the length and width of the grid L. The grid is defined from -L to L. 

 Next is the number of discretized points between -L and L. 
 
 ### Solving the Eigenvalue Problem 
 After user input is calculated it will solve the eigenvalue problem. It uses eigsh from SciPy to do this which returns the amount of 
 eigenvalues and eigenvectors corresponding to "states." The code is currently setup to calculate the "states" amount of lowest eigenvalues 
 so that it gives eigenvalues from smallest to largest. SciPy is necessary here because it has ARPACK subroutines to handle large sparse matrices. 
 
 ### Output
 For the output, instead of the eigenvectors we are instead more concerned with the probability densities. It uses MatPlotLib 
 in order to make contour plots of not only the potentials but also the probability densities. You should see windows open with these 
 figures. You can track the program's progress in the console in which this is ran. 
