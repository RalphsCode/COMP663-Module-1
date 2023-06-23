# Assignment 1 Question 2
# Author: Ralph Godkin

# IMPORTS
import pandas as pd

# Create the DataFrame
cars_df = pd.read_csv("Module-1/Cars.csv")

# Ask user how many rows they want to read
userNum = int(input('\nEnter the number of rows to display: '))

# Subset the first userNum rows of the data frame
selected_rows = cars_df.loc[userNum]

# Print out the requested rows from the DataFrame
print(selected_rows, '\n')

# Find maximum values of the subset)
print(f'Maximum Value in chosen dataframe:  {selected_rows.max()}\n')