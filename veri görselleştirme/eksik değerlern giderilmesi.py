import seaborn as sns
planets=sns.load_dataset("planets")
df=planets.copy()
print(df.head())
## hiç eksik değer veya gözlem var mı diye bakmak için
print(df.isnull().values.any()) ## True çıktı yani var
## hangi değişkende kaçar tane var bulmak için
print(df.isnull().sum())
## değikenlerdeki eksik değerleri 0 yapmak istersek de şunu kullanabiliriz
##df["degisken_ismi"].fillna(0,inplace=True)
df["distance"].fillna(0, inplace= True)
print(df.isnull().sum())

