import matplotlib.pyplot as plt

numberofemp = [13, 200, 250, 300, 350, 400]

rev = [0.4, 0.6, 0.8, 0.7, 0.8, 0.9]

year = [2011, 2012, 2013, 2014, 2015, 2016]

fig, xaxis_1 = plt.subplots()

xaxis_1.plot(year, numberofemp, marker='D', mfc='green', mec='yellow',ms='7')

xaxis_1.set_xlabel('Year')

xaxis_1.set_ylabel('Number of Employees')

xaxis_1.set_title('Number of Employee and Revenue')

# create xaxis_2 with shared x-axis

xaxis_2 = xaxis_1.twinx()

# plot rev on xaxis_2

xaxis_2.plot(year, rev, marker='o', mfc='red', mec='green',ms='7')

xaxis_2.set_ylabel('Rev [$M]')

# setting the legend

fig.legend(['Number of Employee', 'Rev'], loc='upper left')

plt.show()