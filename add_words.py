import pandas as pd
import numpy as np
df = pd.read_excel('a1.ods', header=None)
n=int(input("Сколько слов ты хочешь добавить? "))
print()
for i in range(n):
    engl=input("Введи английское слово на английском ")
    print()
    rus=input("Введи перевод ")
    print()
    df.loc[len(df.index)] = [engl, rus]
df.to_excel('a1.ods',header=None,index=None)