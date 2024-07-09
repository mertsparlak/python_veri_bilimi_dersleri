import seaborn as sns
import matplotlib.pyplot as plt
flights=sns.load_dataset("flights")
df=flights.copy()
print(df.head())
print("********************\n")
df = df.pivot(index="month", columns="year",values="passengers")
print(df)
sns.heatmap(df)
plt.show(df)
