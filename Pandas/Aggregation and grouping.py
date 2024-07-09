import numpy as np
import pandas as pd
import seaborn as sns
## data setlerinin adına erişmek için --> https://github.com/mwaskom/seaborn-data
df=sns.load_dataset("planets")
print(df)
print(df.head())
print(df.shape)
print(df["number"].mean())
print(df["mass"].mean())
print(df["number"].count())
print(df["number"].min())
print(df["number"].max())
print(df["number"].sum())
print(df.describe()) ## describe komutu hepsini tekte verir
print(df.describe().T) ## variable larını da gösterir
print(df.dropna().describe().T) ## dropna getirirsek veri setindeki eksik değerleri almaz
print("***********")
dff=pd.DataFrame({"gruplar":["A","B","C","A","B","C"],"veri":[10,11,52,35,15,27]})
print(dff)
print(dff.groupby("gruplar").mean()) ## groupby gruplaştırır ve bir şey yapmamızı bekler biz de mean kullandık
print(df.head())
print("***********")
print(df.head().groupby("method")["orbital_period"].mean()) ## burada birden fazla grup olduğu için seçmemiz gerekiyor orbitali seçtik biz de
print("***********")
print(df.head().groupby("method")["orbital_period"].describe())
print("***********")
dff=pd.DataFrame({"gruplar":["A","B","C","A","B","C"],"veri1":[10,11,52,35,15,27],"veri2":[100,203,563,902,104,267]}
,columns=["gruplar","veri1","veri2"])
print(dff)
print(dff.groupby("gruplar").aggregate(["min","max",np.median])) ## aggregate ile bir kaç şey seçip işletebiliyoruz
## eğer kullanmak istediğimiz fonksiyonlar pandasta varsa tırnakla yazılır başka fonksiyonlar normal ama yazmasan da olur tırnak ile
print(dff.groupby("gruplar").aggregate({"veri1": "min","veri2": "max"}))## farklı farklı işlemler de yapabiliriz böyle


