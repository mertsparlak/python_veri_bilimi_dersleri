import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
df=tips.copy()
print(df.head())
sns.lmplot(x="total_bill",y="tip",data=df)
plt.show()
sns.lmplot(x="total_bill",y="tip",hue="smoker",data=df)
plt.show()
sns.lmplot(x="total_bill",y="tip",hue="smoker",col="time",data=df)
plt.show()
sns.lmplot(x="total_bill",y="tip",hue="smoker",col="time",row="sex",data=df)
plt.show()