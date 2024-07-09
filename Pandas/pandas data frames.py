import pandas as pd
l=[1,2,3,4,5]
print(l)
print(pd.DataFrame(l,columns=["degisken_ismi"]))
import numpy as np
m=np.arange(1,10).reshape((3,3))
print(m)
print(pd.DataFrame(m,columns=["var1","var2","var3"]))
df=pd.DataFrame(m,columns=["var1","var2","var3"])
df.head()
print(df.columns)
df.columns=["deg1","deg2","deg3"]
print(df.columns)


