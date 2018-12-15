import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

CHANGE_POINT = '2018-09-11'

df = pd.read_csv('./sleep.csv',names=['date','asleep'],na_values='0')
df = df.dropna()

idx = pd.to_datetime(df['date'])
ts = pd.Series(df.asleep.values,index=idx)

ts1 = ts[:CHANGE_POINT]
ts2 = ts[CHANGE_POINT:]
print(ts1.mean())
print(ts2.mean())

label1 = 'Before'
label2 = 'After'

ts1.hist(alpha=0.5,label=label1)
ts2.hist(alpha=0.5,label=label2)
plt.legend()
plt.xlabel('sleeptime')
plt.ylabel('freq')
plt.show()
