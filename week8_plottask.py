# week8_plottask.py
# Week 8 Assignment: Create a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function h(x)=x3 in the range 0 to 10. 
# Author: Faolán Hamilton

# I approached this task in separate sections:
# I started with the first half of the task, setting the normal distribution 
# Then I moved onto setting the range 
# Finally, I moved onto the part that confused me - h(x) = x3

# Import the modules I need:
# Matplotlib will visualise the chart
import matplotlib.pyplot as plt
# Numpy will make the numbers easier to manipulate
import numpy as np

# Histogram plot data

# Setting the mean, standard deviation and value ( in that order in the brackets)
# np.random.normal sets random numbers that results in a normal distribution
normal_distribution = np.random.normal(5, 2, 1000)

# Setting the seed is important, this ensures the random numbers are the same each time
np.random.seed (1)

# Set the plot as a histogram
# Set the number of bins (how many bars representing groups in the data)
# alpha represents the transparency, more important if there are overlapping bars
# the colour (spelt 'color') shows the bar colour
plt.hist(normal_distribution, bins=25, alpha=0.6, color='Purple')

# I was initially confused by h(x) = x3, so I consulted AI on this one, I have quoted the question and answer in references below
def h(x):
    return x**3

# I need to set the range for x, so I will use np.linspace (this method was used in the geeksforgeeks website, reference A)
x = np.linspace(0, 10, 1000)
# Using the AIs help, I know now y
y = h(x)    

# Plot the data - method on geeksforgeeks
plt.plot(x, y)

# C - Making it look nicer 
plt.title("Normal Distribution Histogram")
plt.xlabel("x")
plt.ylabel("h(x) = x3")

# Print the plot, only need to say show() using the matplotlib module
plt.show()

# References
# A - setting mean, std dev, https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
# B - confirms the mean, std dev - numpy.random.Generator.normal - https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html
# C - AI text:
#   My question: Hello, I am trying to plot a histogram on python using these values: Create a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function h(x)=x3 in the range 0 to 10... I have figured out everything else except for h(x) = x3 - what does this mean?
#   Answer: No problem! The function h ( x ) = x 3 h(x)=x 3 means that for any value of x x, the function h ( x ) h(x) will return x x raised to the power of 3. In other words, it's a cubic function. Here's a breakdown: If x = 1 x=1, then h ( 1 ) = 1 3 = 1 h(1)=1 3 =1. If x = 2 x=2, then h ( 2 ) = 2 3 = 8 h(2)=2 3 =8. If x = 3 x=3, then h ( 3 ) = 3 3 = 27 h(3)=3 3 =27. So, for any x x in the range from 0 to 10, you calculate x 3 x 3 to get the corresponding h ( x ) h(x) value. Would you like to see how this function looks when plotted?
#   Follow-up question: So, is h(x) =x3 the x or y axis?
#   Follow-up answer: n the plot, h ( x ) = x 3 h(x)=x 3 represents the y-axis values. Here's how it works: The x-axis values are the input values ranging from 0 to 10. The y-axis values are the output of the function h ( x ) = x 3 h(x)=x 3 for each corresponding x value. So, for each point on the x-axis, you calculate x 3 x 3 to get the corresponding y value. For example, if x = 2 x=2, then h ( 2 ) = 2 3 = 8 h(2)=2 3 =8, so the point (2, 8) would be on the plot. If you have any more questions or need further clarification, feel free to ask!
#   Another question: Can you show me the code you used to create the plot?
#   Another answer (confirmation I did structure mine the correct way): 
'''
#import numpy as np
import matplotlib.pyplot as plt

# Create a normal distribution with 1000 values, mean of 5 and standard deviation of 2
data = np.random.normal(5, 2, 1000)

# Create a histogram of the data
plt.hist(data, bins=30, alpha=0.5, label='Normal Distribution')

# main piece I needed help with 
# Define the function h(x) = x^3
def h(x):
    return x**3

# Generate x values from 0 to 10
x = np.linspace(0, 10, 400)
y = h(x)

# Plot the function h(x)
plt.plot(x, y, color='red', label='h(x) = x^3')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Frequency / h(x)')
plt.legend()

# Show the plot
plt.show()
'''
# D - Intermediate Python - Chapter 1: Matplotlib - https://app.datacamp.com/learn/courses/intermediate-python

#----------End----------#
