# week8_plottask.py
# Week 8 Assignment: Create a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function h(x)=x3 in the range 0 to 10. 
# Author: Faolán Hamilton

# Import the modules I need
# Matplotlib will visualise the chart
import matplotlib.pyplot as plt
# Numpy will make the numbers easier to manipulate
import numpy as np

x = np.array(range(0,10))
y = x * x
plt.hist(x,y)

# Making it look nicer
plt.title("Histogram")
plt.xlabel("")
plt.ylabel("")
plt.legend()

# Print the plot, only need to say show() using the matplotlib module
plt.show()

# References
# A - Intermediate Python - Chapter 1: Matplotlib - https://app.datacamp.com/learn/courses/intermediate-python
#----------End----------