# Assignment 1 Question 1
# Author: Ralph Godkin

# Import numpy and scipy
import numpy as np
import scipy.stats as st

# Set the paramaters
x1 = int(input('Enter first number (press enter for 1): ') or 1)
x2 = int(input('Enter second number (press enter for 6): ') or 6)
x3 = int(input('Enter third number (press enter for 12): ') or 12)
x4 = int(input('Enter fourth number (press enter for 15): ') or 15)

# Define the x and y values
x = np.array([x1, x2, x3, x4])
y = np.array([0, 10, 7, 25])

# Print the result
print('\n', st.linregress(x,y), '\n')
