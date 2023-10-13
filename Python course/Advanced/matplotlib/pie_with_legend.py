import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc  # для вывода русских букв
 
font = {'family': 'Verdana', # для вывода русских букв
        'weight': 'normal'}
       
rc('font', **font)

y = np.array([35, 25, 25, 15])

# метки диаграммы
mylabels = ["Яблоки", "Бананы", "Вишня", "Финики"]

plt.pie(y, labels = mylabels)
plt.show()