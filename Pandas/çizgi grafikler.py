import seaborn as sns
import matplotlib.pyplot as plt
fmri=sns.load_dataset("fmri")
df=fmri.copy()
print(df.head())
print(df.shape)
print(df.groupby("timepoint")["signal"].count())
print(df.groupby("timepoint")["signal"].describe())
sns.lineplot(x="timepoint",y="signal",data=df)
plt.show()
sns.lineplot(x="timepoint",y="signal",hue="event",data=df)
plt.show()
