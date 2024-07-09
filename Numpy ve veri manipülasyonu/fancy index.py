import numpy as np
v=np.arange(0,30,3)
print(v)
print(v[3],v[5],v[7])
al_getir=[3,5,7]
print(v[al_getir]) ##bu yaptığımız işleme fancy index işlemi denir
##iki boyutta fancy de şöyle oluyor -->
print("**************")
m=np.arange(9).reshape((3,3))
print(m)
print("**************")

satir=np.array([1,1])
sutun=np.array([0,2])
print(m[satir,sutun])
print("**************")

##Koşullu eleman işlemleri
v=np.array([1,2,3,4,5,6])
print(v>5)
print(v[v<4]) ##bu şekilde de koşulu sağlayan elemanları getirtebiliyoruz