import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
df=tips.copy()
print(df.head())
sns.scatterplot(x="total_bill",y="tip",data=df)
plt.show()
sns.scatterplot(x="total_bill",y="tip",hue="time",data=df)
plt.show()
sns.scatterplot(x="total_bill",y="tip",hue="day",style="day",data=df)
plt.show()
