import numpy as np
v=np.array([1,2,3,4,5])
print(v-1)
print(v*5)
print(v/5)
#bu işlemleri yaptığımızda aslında ufunc şlemi yapılıyor
print(np.log(v))
## iki bilinmeyenli denklem çözme
#5*x0+x1=12
#x0+3*x1=10
a=np.array([[5,1],[1,3]]) ## katsayıları yazıyoruz yani
b=np.array([12,10]) ## debklemlerin eşit oldukları sayılar
print(a,b)
x=np.linalg.solve(a,b) ##birinci ve ikinci argüman sonucunda oluşacak sayıları buldurur
print(x)
