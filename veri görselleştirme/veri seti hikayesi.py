import seaborn as sns
car_crashes = sns.load_dataset("car_crashes")
df=car_crashes.copy()
print(df.head())
print(df.info)
print(df.describe().T)
print(df.head())
print(df["alcohol"].value_counts())
print(df["speeding"].value_counts())
from pandas.api.types import CategoricalDtype
df.speeding.head()
df.speeding.astype(CategoricalDtype(ordered=True))
print("*******\n")
sns.barplot(x="speeding",y=df.speeding.index,data=df);
