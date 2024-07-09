import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")
df=iris.copy()
print(df.head())
sns.pairplot(df) ## tüm grafikleri verir
plt.show()
sns.pairplot(df,hue="species") ## tüm grafikleri verir
plt.show()
sns.pairplot(df,hue="species",kind="reg") ## tüm grafikleri verir
plt.show()