from scipy.stats import norm
print(norm.cdf(90,80,5)) #ilk argüman hesaplamak isteğimiz değer ikinci ortalamadır ve üçüncü de standart sapma
## 90dan lazma olma olasıılığı bu kadardır
print(norm.cdf(70,80,5)) ##70den fazla olması
