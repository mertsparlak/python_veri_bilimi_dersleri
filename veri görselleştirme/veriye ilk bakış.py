import seaborn as sns
planets = sns.load_dataset("planets")
print(planets.head())
df=planets.copy()
print(df.head())
print(df.tail())
print(df.info())
print(df.dtypes)
import pandas as pd
df.method=pd.Categorical(df.method) ## bu şekilde obje olan methodu kategorik yaptık
print(df.dtypes)
print(df.describe().T)


