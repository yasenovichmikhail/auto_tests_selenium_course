import matplotlib.pyplot as plt

numberofemp_A = [13, 200, 250, 300, 350, 400]

numberofemp_B = [10, 100, 150, 200, 250, 800]

year = [2011, 2012, 2013, 2014, 2015, 2016]

plt.plot(year, numberofemp_A, marker='D', mfc='green', mec='yellow',ms='7')

plt.plot(year, numberofemp_B, marker='o', mfc='red', mec='green',ms='7')

plt.xlabel('Year')

plt.ylabel('Number of Employees')

plt.title('Number of Employee V/s Year Growth')

plt.legend(['numberofemp_A','numberofemp_B'])

plt.show()