import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
df=tips.copy()
print(df.head())
print(df.describe().T)
print(df["sex"].value_counts())
print(df["smoker"].value_counts())
print(df["day"].value_counts())
print(df["time"].value_counts())
sns.boxplot(x=df["total_bill"])
plt.show()
## HANGİ GÜNLER DAHA FAZLA KAZANIYORUZ
sns.boxplot(x="day",y="total_bill",data=df)
plt.show()
## sabah mı akşam mı daha çok kazanıyoruz
sns.boxplot(x="time",y="total_bill",data=df)
plt.show()
## kişi sayısı kazanç
sns.boxplot(x="size",y="total_bill",data=df)
plt.show()
## gün cinsiyet ve kazanç
sns.boxplot(x="day",y="total_bill",hue="sex",data=df)
plt.show()