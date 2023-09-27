# change_colour.py

import matplotlib.pyplot as plt

numberofemp = [13, 200, 250, 300, 350, 400]

year = [2011, 2012, 2013, 2014, 2015, 2016]

plt.plot(year, numberofemp, marker='D', mfc='green', mec='yellow',ms='7')

plt.xlabel('Year')

plt.ylabel('Number of Employees')

plt.title('Number of Employee V/s Year Growth')

plt.show()