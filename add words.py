import pandas as pd
import pickle as pkl
df=pkl.load(open('C:/Users/admin/Desktop/англ/data.pkl.gz', 'rb'))
r=list(input("введите английское слово и его перевод через пробел:  ").split(sep=" "))
r=pd.Series(r)
df=df.append(r, ignore_index=True)
pkl.dump( df, open('C:/Users/admin/Desktop/англ/data.pkl.gz', 'wb'))
pkl.dump( df, open('C:/Users/admin/Desktop/англ/data2.pkl.gz', 'wb'))
