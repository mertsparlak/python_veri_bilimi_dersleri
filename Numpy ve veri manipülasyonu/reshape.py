import numpy as np
print(np.arange(1,10))
print(np.arange(1,10).reshape(3,3)) ##reshape fonksiyonu sayesinde bir listeyi matrix yapabilirsin yani boyut değiştirebilirsin
x=np.array([1,3,5])
y=np.array([2,4,6])
print("********************")
print(np.concatenate([x,y])) ## birleştirmek için concantenate fonksiyonu kullanılır
#iki boyutlu birleştirme için:
k=np.array([[1,2,3],
           [4,5,6]])
j=np.array([[7,8,9],
           [10,11,12]])
print(np.concatenate([k,j]))
print(np.concatenate([k,j],axis=1)) ## axisi default olarak 0 alıyor ama biz 1 yaparsak 2. arrayin 1.si ile birleştiricek
print("********************")

##array ayırma:
n=np.array([1,3,5,7,12,99,99,100])
a,b,c=np.split(n,[3,6])
print(a,b,c)
print("********************")
## iki boyutlu ayırma:
m=np.arange(16).reshape(4,4)
ust,alt=np.vsplit(m,[2])
print("{}\t{}".format(ust,alt))
print("********************")
print(m)
sag,sol=np.hsplit(m,[2])
print(print("{},{}".format(sag,sol))) ## sagdan ve soldan olarak dikeyleme böler
print("********************")
## sıralama:
v=np.array([2,6,0,4,1,5,3])
print(np.sort(v))
print(v)
print(v.sort())
print(v)

## yani np sort arrayi bozmuyor ama normal sort bir kez kullanılınca bozuyor yapıyı ve sıralı halde kalıyor arayimiz
q=np.random.normal(20,10,[3,3]) ##2. girilen değer standart sapma, birinci hangi değerden sapıcağı, üçüncü boyut
print(np.sort(q,axis=0)) #sütunları sıralar kendi içinde yani y ekseni
print(np.sort(q,axis=1)) ## satırları sıralar kendi içinde yani x ekseni


