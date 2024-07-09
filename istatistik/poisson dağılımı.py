from scipy.stats import poisson
lamda_=0.1
rv=poisson(mu=lamda_) ## poissonda mu ile lambdayı belirtmemiz gerekir
print(rv.pmf(k=0)) ## 0 hata olması yani %90 olasılık mantıklı olarak çünkü poissonlar nadir olasılıklardır
print(rv.pmf(k=3))
print(rv.pmf(k=5))