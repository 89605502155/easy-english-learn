import pandas as pd
import numpy as np
import os
import xlrd
import re
from clear import clear
df = pd.read_excel('C:/Users/admin/Desktop/англ/a1.xlsx', header=None)
r=input("хотители вы просмотреть словарь:")
if (r=="да"):
    print(df)
a=[]
v=[]
for i in df.index:
    a+=[df.iloc[i,0]] #столбец английских слов
    v+=[df.iloc[i,1]]  #столбец переводов
print (v)
import random
c=int(input("сколько слов ты хочешь проработать:"))
cc=int(input("сколько подходов сдедаешь:"))
nm=np.random.randint(0,len(a)-1, size=c) #рандомно выбираем промежуток словаря
rr=input("хотители вы просмотреть слова для выучивания:")
if (rr=="да"):
    print( df.iloc[nm,:])
for i in range(0,cc):
    s=random.randint(0,len(nm)-1)
    ty=nm[s]
    print(v[ty])
    r=input()
    if (r==a[ty]):
        print ("Правильно")
    if (r!=a[ty]) and (r!=str(0)):
        h=0
        while ((r!=a[ty])and (r!=str(0))) or (h<15):
            print ("Неравильно")
            print(v[ty])
            r=input()
            if (r==a[ty]):
                print ("Правильно")
                break
            if (h==14):
                print(v[ty]+"- это "+ a[ty])
            h+=1
    if (r==str(0)):
        break
