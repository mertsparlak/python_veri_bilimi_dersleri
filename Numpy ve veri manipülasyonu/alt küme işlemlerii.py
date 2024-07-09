import numpy as np
a=np.arange(20,30)
print(a)
print(a[0:3])## yani a'da 0ıncı indexten 3üncü indexe git
print(a[3:]) ##3üncü indexten sona kadar git demek
print(a[0::2]) ## 0ıncı indexten sona kadar ikişer ikişer
print("***********")
## iki boyutlu slice işlemleri:
b=np.random.randint(10,size=[5,5])
print(b)
print(b[:,2]) ## 2. indexteki sütuna eriştik yani
print(b[0,:]) ## 0. indexteki satıra eriştik
print([b[0:2,0:3]]) ## odan 2 ye kadar satırlar, 0 dan 3 e kadar sütunları alıyor