import seaborn as sns
planets=sns.load_dataset("planets")
df=planets.copy()
print(df.head())
kat_df=df.select_dtypes(include=["object"])
print(kat_df.head())
print(kat_df.head(10))
## kategorik değişkenin sınıflarına ve sayısına erişmek
print(kat_df.method.unique()) ## bunlar sınıfları
print(kat_df["method"].value_counts().count())## bu da sınıflarının sayısı
print(kat_df["method"].value_counts())## kategorik değişkenin sınıflarının frekansına da böyle erişilir
print(df["method"].value_counts().plot.barh())