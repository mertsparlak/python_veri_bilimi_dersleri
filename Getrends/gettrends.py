import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

pytrends = TrendReq()

# List for the keywords for which you want to get trends from Google
td_list = ["python", "java", "javascript", "c++"]

# Build payload
pytrends.build_payload(td_list, cat=0, timeframe="2010-01-01 2022-12-30", geo="TR")

# Get distribution over time
df = pytrends.interest_over_time()

#Transform to Excel sheet
df.to_excel("trends.xls")

# Plot the trends
plt.figure(figsize=(15, 8))
plt.plot(df.index, df["python"], "b*")
plt.plot(df.index, df["java"], "r*")
plt.plot(df.index, df["javascript"], "k*")
plt.plot(df.index, df["c++"], "g*")
plt.legend(["python", "java", "javascript", "c++"])
plt.show()
