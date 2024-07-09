import numpy as np
fiyatlar=np.random.randint(10,110,1000) #ilki başlangıç ikinci son aralık üçüncü kaç tane istendiği
print(fiyatlar.mean())
import statsmodels.stats.api as sms
print(sms.DescrStatsW(fiyatlar).tconfint_mean()) ## gösterdiği iki sayı %95 in alacağı fiyat aralığıdır
## sadece %5lik kesim bu fiyat aralıklarının dışında bir sayı söylemiştir.
