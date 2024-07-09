import pandas as pd
import seaborn as sns
titanic=sns.load_dataset("titanic")
print(titanic.head())
print("Titanic survived oranları: \n{}".format(100*(titanic.groupby("sex")["survived"].mean())))
print("Titanic survived oranları:\n {}".format(100*(titanic.groupby(["sex","class"])[["survived"]].aggregate("mean").unstack())))
print("Titanic survived oranları:\n {}".format(100*(titanic.groupby(["sex","class"])[["survived"]].aggregate("mean"))))
## unstack tablo biçmini değiştirir göründüğü gibi
## ya da kolayca pivot table kullanbiiliriz
print("***********\n")
print("Titanic survived oranları: \n{}".format(100*titanic.pivot_table("survived",index="sex",columns="class")))
print(titanic.age.head())
age=pd.cut(titanic["age"],[0,18,90])
print(age.head(10))
print(titanic.pivot_table("survived",["sex",age],"class"))## katagorik değişken yani age tırnak içinde yazılmamalı
