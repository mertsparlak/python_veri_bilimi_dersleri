import numpy as np
import pandas as pd
m=np.random.randint(1,30,size=(10,3))
df=pd.DataFrame(m,columns=["var1","var2","var3"])
print(df)
## loc: tanımlandığı şekliyle seçim yapmak için kullanılır
print(df.loc[0:3]) ## index 3 ü de dahil ediyor
## iloc:alışık olduğumuz indexleme mantığıyla çalışır
print(df.iloc[0:3]) ## alıştığımız gibi 0 dan 3 e index alımında 3 ü almıyor
print(df.iloc[:3,:2])##ilk girilen sütun ikinci girilen satır için girişir
print(df.loc[0:3,"var3"]) ##böyle ad ile mutlak şekilde bir indeksleme seçeceksek "loc" kullanmalıyız "iloc" hata verir
## verilen kurallara göre indeksleme yapıcaksak iloc eğer kafamıza göreyse loc

print(df[0:2]["var1"])
print(df[df.var1>15]) ## böylelikle koşullu işlemler yapabiliriz dataframes üstünde
print("*******")
print(df[(df.var1>15)&(df.var3<10)])
print(df.loc[(df.var1>20),["var1","var2"]])
print(df[df.var1>20][["var1","var2"]]) ## loc ile de böyle de kullanabiliriz özellikle almak istediğimiz yerleri
