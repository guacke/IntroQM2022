#!/usr/bin/env python
# coding: utf-8

# <h1>Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Part-1;-Final-Exam-CHEM-3PA3;-Winter-2021" data-toc-modified-id="Part-1;-Final-Exam-CHEM-3PA3;-Winter-2021-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Part 1; Final Exam CHEM 3PA3; Winter 2021</a></span><ul class="toc-item"><li><span><a href="#✍️-Write-the-Time-Dependent-Schrödinger-equation-for-one-particle,-in-three-dimensions,-confined-by-the-time-dependent-potential-$V(x,y,z,t)$." data-toc-modified-id="✍️-Write-the-Time-Dependent-Schrödinger-equation-for-one-particle,-in-three-dimensions,-confined-by-the-time-dependent-potential-$V(x,y,z,t)$.-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>✍️ Write the Time-Dependent Schrödinger equation for one particle, in three dimensions, confined by the time-dependent potential $V(x,y,z,t)$.</a></span></li><li><span><a href="#✍️-Write-the-Time-Independent-Schrödinger-equation-for-a-one-electron-atom-with-atomic-number-$Z$-in-atomic-units." data-toc-modified-id="✍️-Write-the-Time-Independent-Schrödinger-equation-for-a-one-electron-atom-with-atomic-number-$Z$-in-atomic-units.-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>✍️ Write the Time-Independent Schrödinger equation for a one-electron atom with atomic number $Z$ in atomic units.</a></span></li><li><span><a href="#🖩-Compute-properties-of-a-photon-with-wavelength-486.1-nm." data-toc-modified-id="🖩-Compute-properties-of-a-photon-with-wavelength-486.1-nm.-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>🖩 Compute properties of a photon with wavelength 486.1 nm.</a></span></li><li><span><a href="#🧮-How-many-quantum-numbers-are-needed-to-label-the-eigenstates-of-the-following-Hamiltonian:" data-toc-modified-id="🧮-How-many-quantum-numbers-are-needed-to-label-the-eigenstates-of-the-following-Hamiltonian:-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>🧮 How many quantum numbers are needed to label the eigenstates of the following Hamiltonian:</a></span></li><li><span><a href="#🔀Below-is-a-list-of-terms-in-the-molecular-Hamiltonian,-together-with-their-mathematical-expressions." data-toc-modified-id="🔀Below-is-a-list-of-terms-in-the-molecular-Hamiltonian,-together-with-their-mathematical-expressions.-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>🔀Below is a list of terms in the molecular Hamiltonian, together with their mathematical expressions.</a></span></li><li><span><a href="#🔀Below-are-lists-of-different-Hamiltonians-we-considered-in-the-course,-together-with-the-names-of-functions-that-are-related-to-their-solutions." data-toc-modified-id="🔀Below-are-lists-of-different-Hamiltonians-we-considered-in-the-course,-together-with-the-names-of-functions-that-are-related-to-their-solutions.-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>🔀Below are lists of different Hamiltonians we considered in the course, together with the names of functions that are related to their solutions.</a></span></li><li><span><a href="#🖩-What-is-the-zero-point-energy-for-an-electron-confined-to-a-2-dimensional-circular-disk-of-radius-$4-\text{-a.u.}$:" data-toc-modified-id="🖩-What-is-the-zero-point-energy-for-an-electron-confined-to-a-2-dimensional-circular-disk-of-radius-$4-\text{-a.u.}$:-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>🖩 What is the zero-point energy for an electron confined to a 2-dimensional circular disk of radius $4 \text{ a.u.}$:</a></span></li><li><span><a href="#✍️-Write-a-Slater-determinant-for-the-excited-state,-$1\text{s}^2-2\text{s}^1-3\text{s}^1$-configuration-of-the-Beryllium-atom." data-toc-modified-id="✍️-Write-a-Slater-determinant-for-the-excited-state,-$1\text{s}^2-2\text{s}^1-3\text{s}^1$-configuration-of-the-Beryllium-atom.-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>✍️ Write a Slater determinant for the excited-state, $1\text{s}^2 2\text{s}^1 3\text{s}^1$ configuration of the Beryllium atom.</a></span></li><li><span><a href="#🧮-Compute-properties-of-a-${}^{7}\text{F}$-state." data-toc-modified-id="🧮-Compute-properties-of-a-${}^{7}\text{F}$-state.-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>🧮 Compute properties of a ${}^{7}\text{F}$ state.</a></span></li><li><span><a href="#✍️-Solve-the-Schrödinger-equation-for-a-muon,-$\mu^-$,-bound-to-Neon-nucleus." data-toc-modified-id="✍️-Solve-the-Schrödinger-equation-for-a-muon,-$\mu^-$,-bound-to-Neon-nucleus.-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>✍️ Solve the Schrödinger equation for a muon, $\mu^-$, bound to Neon nucleus.</a></span></li><li><span><a href="#✍️-Write-an-expression-for-the-lowest-energy-molecular-orbital-of-$\text{H}_3^{+2}$." data-toc-modified-id="✍️-Write-an-expression-for-the-lowest-energy-molecular-orbital-of-$\text{H}_3^{+2}$.-1.11"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>✍️ Write an expression for the lowest-energy molecular orbital of $\text{H}_3^{+2}$.</a></span></li><li><span><a href="#The-next-two-questions-refer-to-the-Laplacian-operator." data-toc-modified-id="The-next-two-questions-refer-to-the-Laplacian-operator.-1.12"><span class="toc-item-num">1.12&nbsp;&nbsp;</span>The next two questions refer to the Laplacian operator.</a></span><ul class="toc-item"><li><span><a href="#✍️-Show-that-$\nabla^2$-is-a-linear,-Hermitian-operator." data-toc-modified-id="✍️-Show-that-$\nabla^2$-is-a-linear,-Hermitian-operator.-1.12.1"><span class="toc-item-num">1.12.1&nbsp;&nbsp;</span>✍️ Show that $\nabla^2$ is a linear, Hermitian operator.</a></span></li><li><span><a href="#✍️-Show-that-$\nabla^2$-is-negative-definite." data-toc-modified-id="✍️-Show-that-$\nabla^2$-is-negative-definite.-1.12.2"><span class="toc-item-num">1.12.2&nbsp;&nbsp;</span>✍️ Show that $\nabla^2$ is negative definite.</a></span></li></ul></li><li><span><a href="#Expectation-values-of-$r^k$-and-related-properties-in-Hydrogenic-atoms." data-toc-modified-id="Expectation-values-of-$r^k$-and-related-properties-in-Hydrogenic-atoms.-1.13"><span class="toc-item-num">1.13&nbsp;&nbsp;</span>Expectation values of $r^k$ and related properties in Hydrogenic atoms.</a></span><ul class="toc-item"><li><span><a href="#✍️-Expectation-value-of-$r^{-1}$-for-Hydrogenic-Atoms." data-toc-modified-id="✍️-Expectation-value-of-$r^{-1}$-for-Hydrogenic-Atoms.-1.13.1"><span class="toc-item-num">1.13.1&nbsp;&nbsp;</span>✍️ Expectation value of $r^{-1}$ for Hydrogenic Atoms.</a></span></li><li><span><a href="#🖩-Expectation-value-of-$r^2$-for-a-4f-orbital-in-the-hydrogen-atom." data-toc-modified-id="🖩-Expectation-value-of-$r^2$-for-a-4f-orbital-in-the-hydrogen-atom.-1.13.2"><span class="toc-item-num">1.13.2&nbsp;&nbsp;</span>🖩 Expectation value of $r^2$ for a 4f orbital in the hydrogen atom.</a></span></li><li><span><a href="#🖩-What-is-the-most-probable-distance-to-find-an-electron-from-the-nucleus-in-the-4f-orbital-of-a-hydrogen-atom?" data-toc-modified-id="🖩-What-is-the-most-probable-distance-to-find-an-electron-from-the-nucleus-in-the-4f-orbital-of-a-hydrogen-atom?-1.13.3"><span class="toc-item-num">1.13.3&nbsp;&nbsp;</span>🖩 What is the most probable distance to find an electron from the nucleus in the 4f orbital of a hydrogen atom?</a></span></li><li><span><a href="#🖩-Heisenberg-Uncertainty-Principle" data-toc-modified-id="🖩-Heisenberg-Uncertainty-Principle-1.13.4"><span class="toc-item-num">1.13.4&nbsp;&nbsp;</span>🖩 Heisenberg Uncertainty Principle</a></span></li><li><span><a href="#💰-Bonus:-Derive-an-expression-for-$\sigma_r^2-\sigma_p^2$-for-any-state-of-a-Hydrogenic-atom-with-$l=n-1$." data-toc-modified-id="💰-Bonus:-Derive-an-expression-for-$\sigma_r^2-\sigma_p^2$-for-any-state-of-a-Hydrogenic-atom-with-$l=n-1$.-1.13.5"><span class="toc-item-num">1.13.5&nbsp;&nbsp;</span>💰 Bonus: Derive an expression for $\sigma_r^2 \sigma_p^2$ for <em>any</em> state of a Hydrogenic atom with $l=n-1$.</a></span></li></ul></li><li><span><a href="#Eigenfunctions-and-Eigenvalues-for-a-two-dimensional-Quantum-Dot." data-toc-modified-id="Eigenfunctions-and-Eigenvalues-for-a-two-dimensional-Quantum-Dot.-1.14"><span class="toc-item-num">1.14&nbsp;&nbsp;</span>Eigenfunctions and Eigenvalues for a two-dimensional Quantum Dot.</a></span><ul class="toc-item"><li><span><a href="#✍️-Write-expressions-for-the-eigenvalues-and-eigenfunctions-of-this-system." data-toc-modified-id="✍️-Write-expressions-for-the-eigenvalues-and-eigenfunctions-of-this-system.-1.14.1"><span class="toc-item-num">1.14.1&nbsp;&nbsp;</span>✍️ Write expressions for the eigenvalues and eigenfunctions of this system.</a></span></li><li><span><a href="#🖩-What-is-the-wavelength-that-corresponds-to-the-lowest-energy-excitation-when-$a_x-=-16$,-$a_y-=-9$,-and-$k_z-=-4$?" data-toc-modified-id="🖩-What-is-the-wavelength-that-corresponds-to-the-lowest-energy-excitation-when-$a_x-=-16$,-$a_y-=-9$,-and-$k_z-=-4$?-1.14.2"><span class="toc-item-num">1.14.2&nbsp;&nbsp;</span>🖩 What is the wavelength that corresponds to the lowest-energy excitation when $a_x = 16$, $a_y = 9$, and $k_z = 4$?</a></span></li></ul></li><li><span><a href="#✍️-What-is-the-form-of-the-eigenfunctions-for-the-Kratzer-Fues-Potential" data-toc-modified-id="✍️-What-is-the-form-of-the-eigenfunctions-for-the-Kratzer-Fues-Potential-1.15"><span class="toc-item-num">1.15&nbsp;&nbsp;</span>✍️ What is the form of the eigenfunctions for the Kratzer-Fues Potential</a></span><ul class="toc-item"><li><span><a href="#💰-Bonus:-Write-an-expression-for-the-energy-eigenvalues-and-the-radial-eigenfunctions-of-the-Kratzer-Fues-potential.-This-isn't-100%-trivial,-but-try-to-see-how-far-you-can-get." data-toc-modified-id="💰-Bonus:-Write-an-expression-for-the-energy-eigenvalues-and-the-radial-eigenfunctions-of-the-Kratzer-Fues-potential.-This-isn't-100%-trivial,-but-try-to-see-how-far-you-can-get.-1.15.1"><span class="toc-item-num">1.15.1&nbsp;&nbsp;</span>💰 Bonus: Write an expression for the energy eigenvalues and the radial eigenfunctions of the Kratzer-Fues potential. This isn't 100% trivial, but try to see how far you can get.</a></span></li></ul></li></ul></li></ul></div>

# # Part 1; Final Exam CHEM 3PA3; Winter 2021
# 
# &#x1f468;&#x200d;&#x1f3eb; **Overview:**
# This is Part 1 of 3 Parts of your Final Exam/Project. 
# - Part 1. Questions on the Course Material. (40%)
# - Part 2. Applying the Course material. (40%)
# - Part 3. Discussing your exam and the Course Material. (20%) 
# 
# **You must submit your Jupyter notebooks for Part 1 and Part 2 at least 48 hours prior to your appointment for Part 3.** You will be given your grade on Part 1 and Part 2 before the oral exam, so that you know what your status is. *For late submission of Part 1 and/or Part 2, I will deduct 2 points per hour.
# 
# 
# &#x1f4dc; **Instructions:**
# Answer the following questions. These are worth 40% of your exam, and each question is worth 2 points. (Some questions have multiple parts.) There is also a bonus problem.
# - You can upload files for mathematical answers or type them in Markdown.
# - You can use the notebook as a calculator for numerical problems; but you can also just type in your answer computed offline.
# - You may find these [sheets containing reference data and mathematical formulas/identities](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/ReferenceConstantsConversionsMath.pdf?raw=true) useful.
# - You may also find it useful to know that the [speed of light, in atomic units](https://en.wikipedia.org/wiki/Hartree_atomic_units), is 137.036 a.u..
# 
# 
# &#x1f4d6; **Rules for "Open Book" Exam:**
# **Like all other portions of this exam, this part of the exam is open notes and open library. It is "open internet search" but you (obviously!) can't post questions on an internet discussion board or homework/problem/exam help site. You are not allowed to communicate with your classmates or any other human being (except me) about these questions or your responses, and this includes human beings (singular or plural, known or anonymous) online.**
# 
# 
# &#x2611;&#xfe0f; **Checklist Before Submission:**
# - Make sure you fill in any place that says YOUR CODE HERE or "YOUR ANSWER HERE". 
# - Remove "Not Implemented Error" where appropriate. 
# - **Please put your name, username (the prefix to your @mcmaster.ca e-mail), and student ID number in the cell below.**
# - Before you turn these problems in, make sure everything runs as expected. 
#   - First, restart the kernel (in the menubar, select Kernel → Restart). 
#   - Then run all cells (in the menubar, select Cell → Run All). 
# - Turn in your exam as a Jupyter notebook.
# 
# 

# In[1]:


Name = "First M. Last"
email_user_name = "username"
ID_number = 1234567

# It's useful to import these libraries. 
# You can import others or not even use these, though.
import numpy as np
import scipy
from scipy import constants


# ## &#x270d;&#xfe0f; Write the Time-Dependent Schr&ouml;dinger equation for one particle, in three dimensions, confined by the time-dependent potential $V(x,y,z,t)$. 
# **Note:** Write out the specific Hamiltonian; do not just write $\hat{H}$. Report your answer in the below markdown cell. You can drag-and-drop a photo/screenshot/image of your answer to the cell, but before submitting please confirm that the image is appropriately embedded.

# YOUR ANSWER HERE

# ## &#x270d;&#xfe0f; Write the Time-Independent Schr&ouml;dinger equation for a one-electron atom with atomic number $Z$ in atomic units.
# **Note:** Report your answer in the below Markdown Cell.

# YOUR ANSWER HERE

# ## &#x1F5A9; Compute properties of a photon with wavelength 486.1 nm.
# The photon emitted when a 4p electron in the Hydrogen atom deexcites into a 2s orbital has wavelength 486.1 nm. Compute its
# - frequency in Hz
# - wavenumber, $\bar{\nu}$, in $\text{cm}^{-1}$.
# - momentum in m kg/s
# - energy in Joules.

# In[2]:


# Give your answers as Floats. I have initialized the variables to None.
frequency = None         #Frequency in Hz.
wavenumber = None        #Wavenumber, nu-bar, in cm^-1
momentum = None          #Momentum in SI units.
energy = None            #Energy in SI units.

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f"The frequency of a photon with wavelength 486.1 nm is {frequency:.3e} Hz.")
print(f"The wavenumber, nu-bar, of a photon with wavelength  486.1 nm is {wavenumber:.3e} cm^-1.")
print(f"The momentum of a photon with wavelength  486.1 nm is {momentum:.3e} kg m/s.")
print(f"The energy of a photon with wavelength  486.1 nm is {energy:.3e} Joules.")

assert(isinstance(frequency,float)), "Type Error: The frequency should be a float."
assert(isinstance(wavenumber,float)), "Type Error: The wavenumber should be a float."
assert(isinstance(momentum,float)), "Type Error: The momentum should be a float."
assert(isinstance(energy,float)), "Type Error: The energy should be a float."


# ## &#x1f9ee; How many quantum numbers are needed to label the eigenstates of the following Hamiltonian:
# $$
# \hat{H} =  -\frac{\hbar^2}{2m}\frac{d^2}{dx_1^2} -\frac{\hbar^2}{2m}\frac{d^2}{dy_1^2}
# -\frac{\hbar^2}{2m}\frac{d^2}{dx_2^2}-\frac{\hbar^2}{2m}\frac{d^2}{dy_2^2}
# + x_1^2 + y_1^2 + x_2^2 + y_2^2
# + e^{-2\left(x_1^2 + y_1^2\right)} + e^{-2\left(x_2^2 + y_2^2\right)} 
# $$

# In[ ]:


# Give your answer as an integer. I have initialized the variable to None
number_of_quantum_nos = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f'The states of this Hamiltonian are labelled with {number_of_quantum_nos} quantum numbers.')

assert isinstance(number_of_quantum_nos,int), "Type error: The answer should be an integer."


# ## &#x1f500;Below is a list of terms in the molecular Hamiltonian, together with their mathematical expressions. 
# Match the verbal description of the term to its mathematical expression; the mathematical expressions are written in atomic units. Report your answer as a dictionary. The keys and values are:
# 
# **Keys:**
# `electronic kinetic energy`, `nuclear kinetic energy`, `electron-electron repulsion potential`, `nucleus-nucleus repulsion potential`, `electron-nuclear attraction potential`
# 
# **Values**:
# "eq1", "eq2", "eq3", "eq4", and "eq5", where
# 
# `eq1`:  $ \sum_{a=1}^{A-1} \sum_{b=a+1}^A \frac{Z_a Z_b}{\left| \mathbf{x}_a - \mathbf{x}_b \right|} $
# 
# `eq2`:  $\sum_{a=1}^A -\tfrac{1}{2m_a} \nabla^2_{\mathbf{x}_a} $
# 
# `eq2`:  $ \sum_{i=1}^N \sum_{a=1}^A -\frac{Z_a}{\left| \mathbf{r}_i - \mathbf{x}_a \right|} $
# 
# `eq4`:  $\sum_{i=1}^N -\tfrac{1}{2} \nabla^2_{\mathbf{r}_i} $
# 
# `eq5`:  $ \sum_{i=1}^{N-1} \sum_{j=i+1}^N \frac{1}{\left| \mathbf{r}_i - \mathbf{r}_j \right|} $
# 
# 
# For example, the following is an example of an *incorrect* answer with the correct format:
# ```
# hamiltonian_terms = {'electronic kinetic energy':'eq1', 'nuclear kinetic energy':'eq2', 'electron-electron repulsion potential':'eq3', 'nucleus-nucleus repulsion potential':'eq4', 'electron-nuclear attraction potential':'eq5'}
# ```

# In[ ]:


# Enter your answer as a dictionary called hamiltonian_terms. 
# The below dictionary has the keys typed in already for you; you need to type in the values eq1, eq2, eq3, eq4, eq5 
#      instead of the place-holder values listed here.
hamiltonian_terms = {'electronic kinetic energy':'eq#', 
                     'nuclear kinetic energy':'eq#', 
                     'electron-electron repulsion potential':'eq#', 
                     'nucleus-nucleus repulsion potential':'eq#', 
                     'electron-nuclear attraction potential':'eq#'}
# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(hamiltonian_terms)

assert len(hamiltonian_terms) == 5, "There should be 5 key:value pairs in the hamiltonian_terms dictionary!"

k = ['electron-electron repulsion potential', 'electron-nuclear attraction potential', 
     'electronic kinetic energy', 'nuclear kinetic energy', 'nucleus-nucleus repulsion potential']
v = ['eq1', 'eq2', 'eq3', 'eq4', 'eq5']
assert sorted(hamiltonian_terms.keys()) == k, "At least one key does not match the original dictionary"
assert sorted(hamiltonian_terms.values()) == v, "At least one value does not match the equation labels"


# ## &#x1f500;Below are lists of different Hamiltonians we considered in the course, together with the names of functions that are related to their solutions. 
# Match each operator with the type of (special) functions that are its eigenfunctions. Report your answer as a dictionary. The keys and values are:
# 
# **Keys:**
# 
# `Ham1`:  $ -\frac{\hbar^2}{2m} \left(\frac{1}{r^2} \frac{d^2}{dr^2} + \frac{1}{r} \frac{d}{dr} - \frac{l^2}{r^2} \right) $
# 
# `Ham2`:  $ - \hbar^2 \left[\frac{1}{\sin \theta}\frac{d}{d\theta}\sin\theta\frac{d}{d\theta} 
# + \frac{1}{\sin^2 \theta} \frac{d^2}{d\phi^2}\right] $
# 
# `Ham3`:  $ -\frac{1}{2} \left( \frac{d^2}{dr^2} + \frac{2}{r} \frac{d}{dr}\right) + \frac{l(l+1)}{2r^2} - \frac{Z}{r} $
# 
# `Ham4`:  $ \frac{d^2}{dx^2} $
# 
# **Values**:
# `associated Laguerre polynomials`, `sines and cosines`, `Bessel functions`, `spherical harmonics`
# 
# For example, the following is an example of an *incorrect* answer with the correct format:
# ```
# eigenfunctions = {'Ham1':'associated Laguerre Polynomials', 'Ham2':'sines and cosines', 'Ham3':'spherical harmonics', 'Ham4':'Bessel functions'}
# ```

# In[ ]:


# Enter your answer as a dictionary called hamiltonian_terms. 
# The below dictionary has the values typed in already for you; you need to type in the keys Ham1, Ham2, Ham3, Ham4 
#      instead of the place-holder values listed here.
eigenfunctions = {'Ham#':'associated Laguerre Polynomials', 
                  'Ham#':'sines and cosines', 
                  'Ham#':'spherical harmonics', 
                  'Ham#':'Bessel functions'}
# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(eigenfunctions)

assert len(eigenfunctions) == 4, "There should be 4 key:value pairs in the eigenfunctions dictionary!"

v = ['Bessel functions', 'associated Laguerre Polynomials', 'sines and cosines', 'spherical harmonics'] 
k = ['Ham1', 'Ham2', 'Ham3', 'Ham4']
assert sorted(eigenfunctions.keys()) == k, "At least one Hamiltonian label does not match the original dictionary"
assert sorted(eigenfunctions.values()) == v, "At least one special function name does not match the original dictionary"


# ## &#x1F5A9; What is the zero-point energy for an electron confined to a 2-dimensional circular disk of radius $4 \text{ a.u.}$:
# - in Hartree atomic units? 
# - in kJ/mol (kiloJoules per mole)?

# In[ ]:


# You can use the code box as a calculator if you like; either way, report your answer as float(s). 
# I've initialized the answers to None.
zero_pt_E_au = None                  #Energy in Hartree (atomic units)
zero_pt_E_kJperMol = None            #Energy in kJ/mol (SI units)

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f'The zero-point energy of a electron confined to a disk of radius 4 Bohr is {zero_pt_E_au:.3f} Hartree.')
print(f'The zero-point energy of a electron confined to a disk of radius 4 Bohr is {zero_pt_E_kJperMol:.3f} kJ/mol.')

# basic tests:
assert(isinstance(zero_pt_E_au,float)), "The answer should be an float"
assert(isinstance(zero_pt_E_kJperMol,float)), "The answer should be an integer"


# ## &#x270d;&#xfe0f; Write a Slater determinant for the excited-state, $1\text{s}^2 2\text{s}^1 3\text{s}^1$ configuration of the Beryllium atom. 
# Assume that the unpaired electrons have the same spin. You may denote the spatial orbitals as $\phi_{1s}(\mathbf{r})$, $\phi_{2s}(\mathbf{r})$ and $\phi_{3s}(\mathbf{r})$.

# YOUR ANSWER HERE

# ## &#x1f9ee; Compute properties of a ${}^{7}\text{F}$ state.
# The ground-state term symbol for Samarium (Sm, atomic number 62) is ${}^{7}\text{F}_0$.
# - How many nominally spatial and spin states are associated with the ${}^{7}\text{F}$ term symbol? Answer with an integer.
# - In addition to J=0, what other J values are possible for the ${}^7{\text{F}}$ term symbol? Answer with a set or list of integers.
# 
# For example, for a triplet P state, we would have 
# ```
# multiplicity_3P = 9
# Jvalues_3P = [0,1,2]
# ```

# In[ ]:


# Multiplicity of septuplet F state of Samarium (integer)
multiplity_7F = None   

# J values associated with septuplet F state of Samarium (set or list of integers)
Jvalues_7F = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f'A septuplet-F term is {multiplicity_7F}-fold degenerate and has J values {Jvalues_7F}.')
      
assert(isinstance(multiplicity_7F,int)), "The multiplicity should be an integer"
assert(isinstance(Jvalues_7F,set) or isinstance(Jvalues_7F,list) or isinstance(Jvalues_7F,tuple)), "The list of J values should be a list of integers."
assert(len(Jvalues_7F) >= 1)
      


# ## &#x270d;&#xfe0f; Solve the Schr&ouml;dinger equation for a muon, $\mu^-$, bound to Neon nucleus.
# In [muonic atoms](https://en.wikipedia.org/wiki/Exotic_atom), a muon replaces an electron. The muon and the electron are both fermions, and they have the same charge. However, the mass of the muon is $207$ times the mass of the electron, $m_\mu = 206.8 m_e$. 
# 
# Assuming the Born-Oppenheimer approximation is valid and that relativistic effects can be neglected, **what are the energy eigenfunctions and eigenvalues for a system composed of one $\mu^-$ bound to a Neon nucleus.** 

# YOUR ANSWER HERE

# ## &#x270d;&#xfe0f; Write an expression for the lowest-energy molecular orbital of $\text{H}_3^{+2}$. 
# You may assume that the system is well-described by the separated-atom limit, and that the Hydrogen atoms are arranged as an equilateral triangle ($\text{D}_{3h}$ symmetry). You do not need to normalize the molecular orbital.

# YOUR ANSWER HERE

# ## The next two questions refer to the Laplacian operator.
# In this question you will show, mathematically, that two properties of the Laplacian operator are true. It is OK (but not essential) to assume that you are interested in the Laplacian operator in 1 dimension, $\nabla^2 = \frac{d^2}{dx^2}$. 
# Note: You may assume that the wavefunction, and its first first and second derivatives, vanish at the ends of the region of integration. However, there are also ways to answer these questions without explicitly invoking those assumptions.
# 
# ### &#x270d;&#xfe0f; Show that $\nabla^2$ is a linear, Hermitian operator.

# YOUR ANSWER HERE

# ### &#x270d;&#xfe0f; Show that $\nabla^2$ is negative definite. 
# That is, show that for *any* $\Psi(\mathbf{r})$, it is *always* true that 
# $$
# \langle \Psi | \nabla^2 | \Psi \rangle < 0
# $$

# YOUR ANSWER HERE

# ## Expectation values of $r^k$ and related properties in Hydrogenic atoms.
# The goal of this problem is to explore the radial distribution function and its expectation values for hydrogenic atoms. A key integral that will be useful is
# $$
# \int_0^{\infty} r^n e^{-\beta r} dr = \frac{n!}{\beta^{n+1}}
# $$
# 
# It is also useful to know [Kramer's recursion relation](https://phlconnect.ched.gov.ph/admin/uploads/81dc9bdb52d04dc20036dbd8313ed055/53-hydrogen-4.pdf) for radial expectation values. If $\psi_{nlm}(r,\theta,\phi)$ denotes a normalized hydrogenic wavefunction, then Kramer's recursion states that:
# $$
# \langle \psi_{nlm} | r^k | \psi_{nlm} \rangle = a_{n}(k,Z) \langle \psi_{nlm} | r^{k-1} | \psi_{nlm} \rangle + b_{nl}(k,Z) \langle \psi_{nlm} | r^{k-2} | \psi_{nlm} \rangle
# $$
# where
# 
# \begin{align}
# a_{n}(k,Z) &=  \frac{n^2(2k+1)}{(k+1)Z}\\
# b_{nl}(k,Z) &= \frac{n^2 k \left(k^2 - (2l+1)^2\right)}{4Z^2(k+1)}
# \end{align}
# A detailed derivation of this relation can be found [here](http://www.blazartheory.com/files/notes/qmnotes/Kramers__Relation.pdf). You will not *need* to use this relation in this problem; it's a matter of preference whether you use this relation or perform integrals.
# 
# Throughout this problem you may use atomic units.

# ### &#x270d;&#xfe0f; Expectation value of $r^{-1}$ for Hydrogenic Atoms.
# What is the expectation value of $r^{-1}$ for a Hydrogenic atom. That is, what is the expectation value of 
# $$
# \langle \psi_{nlm} | r^{-1} | \psi_{nlm} \rangle
# $$
# for an electron bound to a nuclear of charge Z. *Report your answer as a float, in atomic units.*

# YOUR ANSWER HERE

# ### &#x1F5A9; Expectation value of $r^2$ for a 4f orbital in the hydrogen atom.
# What is the expectation value of $r^2$ for the 4f orbital in the hydrogen atom (Z=1). That is, what is the expectation value of 
# $$
# \langle \psi_{43m} | r^2 | \psi_{43m} \rangle
# $$
# in the Hydrogen atom? *Report your answer as a float, in atomic units.*
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[ ]:


# Expectation value of r^2 for a 4f orbital in the hydrogen atom (Z=1) in atomic units (Bohr^2). 
# I have initialized the variable to None. Give your answer in atomic units (Bohr).
avg_r2 = None    

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f'The expectation value of r^2 for an electron in the 4f orbital of the hydrogen atom is {avg_r2:.2f} Bohr^2.')


# YOUR ANSWER HERE

# ### &#x1F5A9; What is the most probable distance to find an electron from the nucleus in the 4f orbital of a hydrogen atom?
# Report your answer in Bohr (atomic units).
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[ ]:


# Most probable distance at which to observe an electron in the 4f orbital from the nucleus of the hydrogen atom.
# I have initialized the variable to None. Give your answer in atomic units (Bohr).
dist_mostprob = None    

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f'The most probable value of the distance from the nucleus for a 4f electron in Hydrogen is {dist_mostprob:.2f} Bohr.')


# YOUR ANSWER HERE

# ### &#x1F5A9; Heisenberg Uncertainty Principle 
# The Heisenberg Uncertainty Principle between momentum and position in 3 dimensions states that 
# $$
# \sigma_r^2 \sigma_p^2 \ge  \tfrac{3}{4} \hbar^2
# $$
# where
# $$
# \sigma_r^2 = \langle \psi_{n,n-1,m} | r^2 | \psi_{n,n-1,m} \rangle - \langle \psi_{n,n-1,m} | r | \psi_{n,n-1,m} \rangle^2 \\
# \sigma_p^2 = \langle \psi_{n,n-1,m} | \hat{p}^2 | \psi_{n,n-1,m} \rangle - \langle \psi_{n,n-1,m} | \hat{p} | \psi_{n,n-1,m} \rangle^2
# $$
# To reassure yourself that this is true, compute $\sigma_r^2 \sigma_p^2$ for the 4f state of the hydrogen atom. *Report your answer as a float, in atomic units.*
# 
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[ ]:


# Write the left-hand-side of the Heisenberg Uncertainty relation, which should be bigger than 3/2 hbar.
# Give your answer in atomic units.
test_Heisenberg = None    

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f'The product of the variance in position and momentum for an electron in the 4f orbital of Hydrogen is {test_Heisenberg:.2f} times hbar.')
assert(test_Heisenberg >= 0.75), "The Heisenberg Uncertainty Principle has been violated!"


# YOUR ANSWER HERE

# ### &#x1f4b0; Bonus: Derive an expression for $\sigma_r^2 \sigma_p^2$ for *any* state of a Hydrogenic atom with $l=n-1$. 

# YOUR ANSWER HERE

# ## Eigenfunctions and Eigenvalues for a two-dimensional Quantum Dot.
# Modern displays often use quantum dot technology, where one (or more) electrons are confined to a region within a material. For an electron confined to a rectangular region in two dimensions, it is reasonable to approximate its motion perpendicular to the rectangle with harmonic confinement. The time-independent Schr&ouml;dinger equation, eigenfunctions, and eigenvalues for a harmonically confined electron are, in atomic units:
# $$
# \left(-\tfrac{1}{2}\tfrac{d^2}{dz^2} + \tfrac{1}{2}\kappa z^2\right) \psi_k(z) = E_k \psi_k(z)
# $$
# where the eigenenergies are
# $$
# E_k = \sqrt{\kappa}\left(k+\tfrac{1}{2}\right) \qquad \qquad k=0,1,2,\ldots
# $$
# and the eigenfunctions are given in terms of the [Hermite polynomials](https://en.wikipedia.org/wiki/Hermite_polynomials), $H_k(z)$, as:
# $$
# \psi_k^{(\text{harm. osc.})}(z) =\frac{1}{2^k k!}\sqrt[4]{\frac{\kappa}{\pi}}
# e^{-\sqrt{\kappa}z^2/2}H_k\left(\sqrt[4]{\kappa}z\right)
# $$
# The Hamiltonian for an electron confined to a rectangular region, in atomic units, is then:
# $$
# \hat{H} = -\frac{1}{2} \frac{d^2}{dx^2} -\frac{1}{2} \frac{d^2}{dy^2} -\frac{1}{2} \frac{d^2}{dz^2} 
#  + V_{a_x}(x) + V_{a_y}(y) + \frac{1}{2} \kappa z^2
# $$
# where
# $$
# V_a(x) = 
# \begin{cases}
#     +\infty & x\leq 0\\
#     0       & 0\lt x \lt a\\
#     +\infty & a \leq x
# \end{cases}
# $$
# 
# ### &#x270d;&#xfe0f; Write expressions for the eigenvalues and eigenfunctions of this system.
# 

# YOUR ANSWER HERE

# ###  &#x1F5A9; What is the wavelength that corresponds to the lowest-energy excitation when $a_x = 16$, $a_y = 9$, and $k_z = 4$?
# Report your answer in nm. 
# 
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[ ]:


# Report the wavelength of the lowest-energy excitation in nm. I have initialized the variable to None.
wavelength_qdot_nm = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f'The wavelength associated with the lowest-energy excitation of the specified quantum dot is {wavelength_qdot_nm:.1f} nm.')


# YOUR ANSWER HERE

# ## &#x270d;&#xfe0f; What is the form of the eigenfunctions for the Kratzer-Fues Potential
# The Kratzer-Fues potential is a reasonable model for a diatomic molecule rotating and vibrating in 3 dimensions, or even a ion-pair complex (e.g., an single ion pair from an ionic solvent in the gas phase). It has the form
# $$
# V_{\text{Kratzer-Fues}}(r) = \frac{a}{r^2} - \frac{b}{r} \qquad \qquad a>0 \text{ and } b>0
# $$
# and so the Schr&ouml;dinger equation has the form:
# $$
# \left(-\frac{\hbar^2}{2m}\nabla^2 +\frac{a}{r^2} - \frac{b}{r} \right) \psi(\mathbf{r}) = E\psi(\mathbf{r}) 
# $$
# Using separation of variables, write the *form* of the solutions for the Kratzer-Fues potential. What is the radial Schr&ouml;dinger equation for this system?

# YOUR ANSWER HERE

# ### &#x1f4b0; Bonus: Write an expression for the energy eigenvalues and the radial eigenfunctions of the Kratzer-Fues potential. This isn't 100% trivial, but try to see how far you can get.
# 

# YOUR ANSWER HERE