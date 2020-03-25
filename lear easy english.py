import pandas as pd
import numpy as np
import os
df = pd.read_excel('C:/Users/admin/Desktop/англ игра/a1.xlsx', header=None)
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
for i in range(0,c):
    s=random.randint(0,len(a)-1)
    print(v[s])
    r=input()
    if (r==a[s]):
        print ("Правильно")
    if (r!=a[s]) and (r!=str(0)):
        h=0
        while ((r!=a[s])and (r!=str(0))) or (h<15):
            print ("Неравильно")
            print(v[s])
            r=input()
            if (r==a[s]):
                print ("Правильно")
                break
            if (h==14):
                print(v[s]+"- это "+ a[s])
            h+=1
    if (r==str(0)):
        break
