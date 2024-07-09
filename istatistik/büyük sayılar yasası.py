import numpy as np
rng=np.random.RandomState(123) ## random state işlemleri sabitlemek için kullanılır
for i in np.arange(1,21):
    deney_sayisi=2**i
    yazi_turalar=rng.randint(0,2,size=deney_sayisi)
    yazi_olasiliklari=np.mean(yazi_turalar)
    print("atış sayısı:",deney_sayisi,"----","yazi olasılığı:%.2f"%(yazi_olasiliklari*100))
