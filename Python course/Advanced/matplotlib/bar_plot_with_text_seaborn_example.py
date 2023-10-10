import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

continent = ["Africa","Americas","Asia","Europe","Oceania"]
lifeExp=[49,65,60,72,74]

df = pd.DataFrame({"continent":continent, "lifeExp":lifeExp})


#bar label is placed in the middle of the bars

plt.figure(figsize=(8, 6))
splot=sns.barplot(x="continent",y="lifeExp",data=df)
plt.xlabel("Continent", size=16)
plt.ylabel("LifeExp", size=16)
plt.bar_label(splot.containers[0],size=16,label_type='center')
# plt.savefig("annotate_barplot_with_Matplotlib_bar_label_at_center_Python.png")

# bar label is placed above the bars

plt.figure(figsize=(8, 6))
splot=sns.barplot(x="continent",y="lifeExp",data=df)
plt.xlabel("Continent", size=16)
plt.ylabel("LifeExp", size=16)
plt.bar_label(splot.containers[0],size=16)
# plt.savefig("annotate_barplot_with_Matplotlib_bar_label_change_size_Python.png")
plt.show()