# Author : Gaurav
# Case Study 3
# plot a Bar Graph of the data, taking the Year as the x-axis and the number of hurricanes occurring as the Y-axis.


import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("Hurricanes.csv")
df = pd.DataFrame(data)

print("########################## Problem 1 ##########################")
plt.bar(df["Year"],df["Hurricanes"])
plt.show()
#
# The dataset given, records data of city temperatures over the years’2014 and 2015.
# Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow