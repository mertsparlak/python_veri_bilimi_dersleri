import pandas as pd

print(pd.read_csv("ornekcsv.csv"))
print(pd.read_csv("ornekcsv.csv",sep=";")) ## noktalı virgülden ayırınca daha oturaklı durdu
print(pd.read_csv(r"C:\Users\merts\PycharmProjects\python_numpy_pandas\reading_data/duz_metin.txt"))
print(pd.read_excel(r"C:\Users\merts\PycharmProjects\python_numpy_pandas\reading_data\ornekx.xlsx"))
df = pd.read_excel(r"C:\Users\merts\PycharmProjects\python_numpy_pandas\reading_data\ornekx.xlsx")
print(df.head())
print(df.columns)
df.columns=("A","B","C")
print(df.head())
tips=pd.read_csv(r"C:\Users\merts\PycharmProjects\python_numpy_pandas\reading_data\data.txt")
print(tips.head())