import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')

#a)
colors=['pink', 'hotpink', 'deeppink']
mtcars.groupby(['cyl']).mean().plot.bar(y='mpg', title= "Zad2.a) Potrošnju automobila s 4, 6 i 8 cilindara", stacked=True, xlabel='Broj cilindara', ylabel='Potrosnja', color=colors, rot=0)
plt.show()

#b)
boxplot= mtcars.boxplot(by='cyl', column=['wt'], color='pink', boxprops=dict(color='hotpink'))
plt.show()

#c)
colors1=['pink', 'hotpink']
x_labels = ['Automatski', 'Ručni']
ax = mtcars.groupby(['am']).mpg.mean().plot.bar(stacked=True, title='Potrošnja s obzirom na mjenjač', ylabel='Potrošnja', xlabel='Mjenjač', rot=0, color = colors1)
ax.set_xticklabels(x_labels)
plt.show()

#d)
automatic = mtcars[mtcars.am == 0]
manual = mtcars[mtcars.am == 1]
a = automatic[['hp','qsec']].to_numpy()
m = manual[['hp','qsec']].to_numpy()

fig = plt.figure()
ax2 = fig.add_axes([0.1,0.1,0.8,0.8])
axa_hp = ax2.scatter(a[:,1],a[:,0], color = 'pink')
axm_hp = ax2.scatter(m[:,1],m[:,0], color = 'hotpink')
ax2.legend(labels = ['Automatski','Ručni'])
ax2.set_title("Ubrzanje s obzirom na konjsku snagu")

plt.show()