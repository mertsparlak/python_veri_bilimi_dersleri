import pandas as pd
df=pd.DataFrame({"gruplar":["A","B","C","A","B","C"],
                 "degisken1":[10,23,33,22,11,99],
                 "degisken2":[100,253,333,262,111,969]},columns=["gruplar","degisken1","degisken2"])
print(df)
def filter_func(x):
    return x["degisken1"].std()>9
print(df.groupby("gruplar").std())
print(df.groupby("gruplar").filter(filter_func))
## filtrelemek için bir fonksiyon yaratıp o fonksiyonu filter groupbyda kullanırsak böyle istediğimiz gibi filtreleyebişiriz.
print("*******")
print(df["degisken1"]*9) ##burada yaptığımız çarpım 9 gibi fonksiyon yapıp da yapabiliriz böyle şeyleri
df_a=df.iloc[:,1:3]
print(df_a)
print(df_a.transform(lambda x:(x-x.mean())/x.std()))
df=pd.DataFrame({
                 "degisken1":[10,23,33,22,11,99],
                 "degisken2":[100,253,333,262,111,969]},columns=["degisken1","degisken2"])
print(df)
import numpy as np
print(df.apply(np.sum))
print(df.apply(np.mean))
df=pd.DataFrame({"gruplar":["A","B","C","A","B","C"],
                 "degisken1":[10,23,33,22,11,99],
                 "degisken2":[100,253,333,262,111,969]},columns=["gruplar","degisken1","degisken2"])
print(df.groupby("gruplar").apply(np.mean))
print(df.groupby("gruplar").apply(np.sum)) ## böyle yine groupby ile de kullanabiliriz 
