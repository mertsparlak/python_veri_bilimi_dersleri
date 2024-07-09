import seaborn as sns
planets=sns.load_dataset("planets")
df=planets.copy()
print(df.head())
print("******************\n")
df_num=df.select_dtypes(include=["float64","int64"])
print(df_num.head())
print(df_num.head().describe().T)
print(df_num["distance"].head().describe().T)
## türkçeleştirmek için şunu yapabiliriz
print("Medyan: "+str(df_num["distance"].median()))