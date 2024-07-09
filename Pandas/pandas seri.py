import pandas as pd
print(pd.Series([1,2,3,4,5]))
seri=pd.Series([1,2,3,4,5])
print(type(seri))
## index değiştirme
print(pd.Series([1,24,57,4,76]))
print(pd.Series([1,24,57,4,76],index=[1,3,7,9,12]))
print(pd.Series([1,24,57,4,76],index=["a","b","c","d","e"]))
serii=pd.Series([1,24,57,4,76],index=["a","b","c","d","e"])
print(serii["a":"c"])
print(pd.concat([serii,seri]))
seri1=pd.Series([1,7,12,48],index=["ref","rej","cot","rf"])
seri1["rej"]=130
print(seri1)
