import random
import pandas as pd

import numpy as np
s1=np.random.randint(10,size=5)
s2=np.random.randint(10,size=5)
s3=np.random.randint(10,size=5)
sozluk={"var1":s1,"var2":s2,"var3":s3}
print(sozluk)
df=pd.DataFrame(sozluk)
print(df)
print(df[0:1])
df.index=["a","b","c","d","e"]
print(df)
print(df.drop("a",axis=0)) ## a indexini siler
print(df) ## ama kalıcı silmiyor
print(df.drop("a",axis=0,inplace= True)) ##inplace argümanını kullanırsak kalıcı siliyor
print(df)
## fancy ile silme
l=["c","e"]
print(df.drop(l,axis=0))

l=["var1","var2","var4"]
for i in l:
    print(i in df)

print(df["var1"])
df["var4"]=df["var1"]/df["var2"] ##böyle kolayca yeni bir variable de ekleyebiliriz
print(df)
print(df.drop("var4",axis=1))
print(df.drop("var4",axis=1,inplace= True)) ## böyle y ekseninden yani variableslardan da silebiliriz, axis=1 olmalı
print(df)



