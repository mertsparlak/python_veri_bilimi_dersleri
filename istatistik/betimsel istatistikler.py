import seaborn as sns
import researchpy as rp
tips = sns.load_dataset("tips")
df = tips.copy()
print(df.head())
print(df.describe().T)
print(df[["tip","total_bill"]].cov()) ## kovaryason: iki değişkenin birbirine göre nasıl hareket ettiğini ölçer
print(df[["tip","total_bill"]].corr()) ## korelasyon: iki değikenin birbirine göre nasıl değiştiği

