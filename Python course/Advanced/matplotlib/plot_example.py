import matplotlib.pyplot as plt

# X and Y data

numberofemp = [13, 200, 250, 300, 350, 400]

year = [2011, 2012, 2013, 2014, 2015, 2016]

# plot a line chart

plt.plot(year, numberofemp,'*-b')

# set label name of x-axis title

plt.xlabel('Year')

# set label name of x-axis title

plt.ylabel('Number of Employees')

# set label name of chart title

plt.title('Number of Employee V/s Year Growth')

plt.show()