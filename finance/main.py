import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from finance.functions import rescale

np.random.seed(123456)

# POINTS = 100
#
# ts = pd.Series(np.random.randn(POINTS), index=pd.date_range('1/1/2000', periods=POINTS))
#
# df = pd.DataFrame(30*np.random.randn(POINTS, 4)+100, index=ts.index, columns=list('ABCD'))
#
# plt.figure()
# df.plot(y='B')
# plt.show()
#
# df['B'] = rescale(df['B'])
#
# plt.figure()
# df.plot(y='B')
# plt.show()


#------------------------------------------------------

ticker = ['data/historical/Stocks/aapl.us.txt', 'data/historical/Stocks/yelp.us.txt']
df = pd.read_csv(ticker[1], engine='python')
print(df.head(4))
print(df.tail(4))


plt.figure()
df.plot(y='Close')
plt.show()

df['Close'] = rescale(df['Close'])

plt.figure()
df.plot(y='Close')
plt.show()

