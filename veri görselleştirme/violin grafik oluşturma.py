import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
df=tips.copy()
print(df.head())
sns.catplot(y="total_bill",kind="violin",data=df)
plt.show()
sns.catplot(x="day",y="total_bill",kind="violin",data=df)
plt.show()
sns.catplot(x="day",y="total_bill",hue="sex",kind="violin",data=df)
plt.show()