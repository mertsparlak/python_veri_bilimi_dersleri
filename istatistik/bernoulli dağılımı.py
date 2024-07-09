from scipy.stats import bernoulli
p=0.6 ## tura gelme olasılığını 0.6 olarak bildiğimizi kabul ettik
rv= bernoulli(p)
print(rv.pmf(k=1)) ## tura gelme olasılığı
print(rv.pmf(k=0)) ## yazı gelme olasılığı
