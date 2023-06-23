# Assignment 1 Question 6
# Author: Ralph Godkin

# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Retrieve the data
titanic = pd.read_csv("Module-1/titanic.csv")

# subset the titanic dataset to include first class male passengers over 18 years old
df = titanic[titanic.pclass == 1][titanic.age > 17.9][titanic.sex == 'male']
# print(f'DataFrame shape: {df.shape}')

# Set title
plt.title('1st Class Males, by Embark Port, Survival Status', fontsize=12)

# Set x-axis label
plt.xlabel('Embark Town')

# Set custom x-axis tick labels
custom_labels = ['Southampton', 'Cherbourg', 'Queenstown']
plt.gca().set_xticklabels(custom_labels)

# Define plot
sns.stripplot(x="embarked", y="age", jitter=True, hue="survived", data=df)

# Show the image
plt.show()