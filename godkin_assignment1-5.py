# Assignment 1 Question 5
# Author: Ralph Godkin

# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get the data
target = pd.read_csv("Module-1/target.csv")

# subset the last 19 days of the dataframe
tgt_march = target.tail(19)
# print(tgt_march)

# subset tgt_march and create a data frame that contains the columns: Date and Volume
tgt_vol = tgt_march[["Date", "Volume"]]
# print(f'The Volume DataFrame Shape: {tgt_vol.shape}\n')
# print(tgt_vol)


# subset tgt_march and create a data frame that contains the columns: Date and Closing
tgt_close = tgt_march[["Date", "Close"]]
# print(f'The Closing Price DataFrame Shape: {tgt_close.shape}\n')
# print(tgt_close)

# *****************************************************************************
# Code to see the Volume for a specific day

day = int(input('Please enter a day to see the Target Volume: ') or 17) - 1

# # subset the specific row of tgt_vol for the given day
volume_row = tgt_vol[day:(day+1)]
print(f'\nVolume for target day: \n{volume_row}\n')
# # gets the volume for the given day
volume = volume_row.iloc[0][1] 
print(f'Volume on that day: {volume}\n')

# # subset the specific row of tgt_close for the given day
close_row =  tgt_close[day:(day+1)]
print(f'Closing Price for that day: \n{close_row}\n')
# gets the closing stock price for the given day
close = close_row.iloc[0][1] 
print(f'Closing Price that day: {close}')

# date = tgt_march.iloc[[day]].iloc[0][0] # gets the date
# print(date)


# *****************************************************************************
# Create line chart for Daily Volume

# Set title
plt.title('Stock Volume', fontsize=20)

# Set x and y axis labels
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel("Volume (10's of Millions)")

# Define plot
plt.plot(tgt_vol["Date"], tgt_vol["Volume"])

# Show the image
plt.show()


# *****************************************************************************
# Create line chart for Closing Price

# Set title
plt.title('Closing Price', fontsize=20)

# Set x and y axis labels
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.ylabel('Closing Price (US$)')

# Define plot
plt.plot(tgt_close["Date"], tgt_close["Close"])

# Show the image
plt.show()