import numpy as np
##numpy veriyi bir tane olarak tutar mesela bu liste integer gibi ama normal liste ile tutmak mesela burada 4 ayrı veri için de listede ayrı yer tutardı
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(a*b)
print(type(a))
c=np.array([3.14,3,5,7])
print(c) ##hepsini ondalıklı yaptı biri ondalıklı diye işte bu numpyın tek tip yapma baskısı
d=np.array([3.14,3,5,7], dtype="int") ##bu şekilde dtype komutu ile arrayimizi hangi tipte alıcağını da belirleyebiliriz.
print(d)
## sıfırdan array oluşturma:
e=np.zeros(10,dtype="int")
print(e)
f=np.ones((3,5),dtype="int")
print(f) ## böyle matrix de oluşturabiliriz yani 3 e 5 lik birim matrix
g=np.full((3,5),3) ## matrixe yazdırmak istediğimiz sayıyı böyle de belirtebiliriz
print(g)
print(np.arange(0,31,3))
print(np.linspace(0,1,10)) ## o ile 1 arası 10 değer oluştur demek
print(np.random.randint(0,10,(3,3))) ## 3 e 3 bir matrix oluşturur belirlediğimiz aralıktan rastgele sayılarla