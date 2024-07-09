##import pip
##pip.main(['install', 'pandas_datareader'])
import pandas_datareader as pr
import seaborn as sns
from datetime import datetime
df = pr.get_data_yahoo('AAPL', start=datetime(2017, 8, 13), end=datetime(2017, 8, 14))
print(df.head())
