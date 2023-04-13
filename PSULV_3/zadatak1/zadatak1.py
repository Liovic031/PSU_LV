import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')
#a)
print("\nA) Kojih 5 automobila ima najveću potrošnju?\n", mtcars.sort_values(by=['mpg'].tail(5)))
#b)
print("\nB) Koja tri automobila s 8 cilindara imaju najmanju potrošnju?\n", mtcars[mtcars.cyl == 8].sort_values('cyl', ascending=True).tail(3))
#c)
cyl_cars = mtcars[mtcars.cyl == 6]
print("\nC) Kolika je srednja potrošnja automobila sa 6 cilindara?\n", cyl_cars['mpg'].mean())
#d)
srednjavjd = mtcars[(mtcars.wt>=2) & (mtcars.wt<=2.2) & (mtcars.cyl==4)]
print("\nD) Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?\n", srednjavjd['mpg'].mean())
#e
autmj_cars = mtcars[mtcars.am==1]
print("\nE Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?\n", autmj_cars['am'].count())
#f)
normj_cars=mtcars[mtcars.am==0]
print("\nF) Broj automobila bez automatskog mjenjača:\n", normj_cars['am'].count())
#g)
autsnag_cars=mtcars[(mtcars.am==1) & (mtcars.hp>100)]
print("\nG) Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga\n", autsnag_cars['hp'].count())
#h)
print("\nH) Kolika je masa svakog automobila u kilogramima?\n")
mtcars['kg']=mtcars.wt * 1000 * 0.45359237
print("\n")