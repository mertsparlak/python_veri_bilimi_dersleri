from scipy.stats import binom
## bir reklama tıklanma olasılığını binom ile hesaplama
## p olasılığımız tıklama için ve n de yapacağımız deneme sayısı
p=0.01
n=100
rv=binom(n,p)
print(rv.pmf(1))##pmf probality mass faction demek hesaplamayı yapıyor yani 1 kişinin tıklama olasılığı
print(rv.pmf(5)) ## 5 kişi tıklama olasılığı
print(rv.pmf(10)) ## 10 kişi tıklama olasılığı

