# Assignment 1 Question 3
# Author: Ralph Godkin

# IMPORTS
import pandas as pd

# Create the DataFrame
cars_df = pd.read_csv("Module-1/mtcars.csv")

# Ask user how many cylinders they wish to locate
cylinders = int(input('\nEnter the number of cylinders to locate: '))

# Subset the requested cylinder cars from the data frame
df_cyl = cars_df[cars_df.cyl == cylinders] # create a new dataframe with only the rows where cyl = cylinders

# Print out the requested rows from the DataFrame
# print(df_cyl, '\n')

# Print out the size of the requested DataFrame
print(f'\nThe size of the DataFrame for {cylinders} cylinders is: ', df_cyl.shape, '\n')