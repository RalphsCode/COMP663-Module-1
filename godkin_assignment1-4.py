# Assignment 1 Question 4
# Author: Ralph Godkin

# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Retrieve the data
titanic = pd.read_csv("Module-1/titanic.csv")

# ==================================================================================
# ***  1st Class By Sex Bar Chart **************************************************
# ==================================================================================

# subset the titanic dataset to include first class passengers who embarked in Southampton
first_south = titanic[titanic.pclass == 1][titanic.embarked == 'S']
# print(first_south.head())

# Set the style of the bar charts
sns.set_theme(style="whitegrid", color_codes=True)

# Set title
plt.title('1st Class Passengers who embarked in Southampton by Sex', fontsize=12)

# Generate a vertical bar chart
sns.countplot(x="class", hue="sex", data= first_south)

# Display the bar chart
plt.show()


# ==================================================================================
# *****  2nd & 3rd Class by Survival ***********************************************
# ==================================================================================

# subset the titanic dataset to include either second or third class passengers
second_third =  titanic[titanic.pclass != 1 ]
# print(second_third.head())

# Set the style of the bar charts
sns.set_theme(style="whitegrid", color_codes=True)

# Set title
plt.title('3rd & 2nd Class passengers who survived', fontsize=12)

# Generate a vertical bar chart
sns.countplot(x="class", hue="survived", data= second_third)

# Display the bar chart
plt.show()