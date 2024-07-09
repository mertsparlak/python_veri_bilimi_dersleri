import numpy as np
a=np.random.randint(10,size=10)
print(a.ndim) ## n.dim fonksiyonu boyutunu söyler arrayin
print(a.shape)## shape fonksiyonu boyut bilgisi verir
print(a.size)#toplam eleman sayısını veriri
print(a.dtype)#array veri tipini verir
b=np.random.randint(10,size=(3,5))
print(b.shape)
print(b.ndim)
print(b.size)
print(b.dtype)


