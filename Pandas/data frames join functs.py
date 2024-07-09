import numpy as np
import pandas as pd
m=np.random.randint(1,30,size=(5,3))
df1=pd.DataFrame(m,columns=["var1","var2","var3"])
print(df1)
df2=df1+88
print("********")
print(pd.concat([df2,df1],ignore_index=True)) ## concat funct is able to union the data frames
## if variables isnt same in both of them, concat will raise error
print(pd.concat([df2,df1],ignore_index=True,join="inner")) ## but if we use the join=inner funct it wont raise error
print("*********")
df3=pd.DataFrame({"Calisanlar":["Ali","Ayşe","Veli","Mert"],"grup":["Muhasebe","mühendis","İK","mühendis"]})
df4=pd.DataFrame({"Calisanlar":["Ali","Ayşe","Veli","Mert"],"ilk giris":[2002,2020,2009,2017]})
print(df3)
print(df4)
print(pd.merge(df4,df3))


