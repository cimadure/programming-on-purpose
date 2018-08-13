import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from finance.functions import rescale, last_maximum_occurrence_index, rescale_timestamp_by_position

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

tickers = ['data/historical/Stocks/aapl.us.txt', 'data/historical/Stocks/yelp.us.txt']
for ticker in tickers:
    df = pd.read_csv(ticker, engine='python',  parse_dates=['Date'])
    #print(df.head(4))
    #print(df.tail(4))

    #index = last_maximum_occurrence_index(df['Close'])
    index = df['Close'].idxmax()

    df['stamp'] = rescale_timestamp_by_position(df['Date'], index)

    plt.figure()
    df.plot(y='Close', title=ticker)
    #plt.plot(index, df['Close'][index], 'rx')
    plt.show()

    df['Close'] = rescale(df['Close'])

    plt.figure()
    df.plot(x='stamp', y='Close')
    plt.plot(df['stamp'][index], df['Close'][index], 'rx')
    plt.show()




    #index = df['Close'].idxmax()

    print("---+", index, df['Close'][index], df['Date'][index])
