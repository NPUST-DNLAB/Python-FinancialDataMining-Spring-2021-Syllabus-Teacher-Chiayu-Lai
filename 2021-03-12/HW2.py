Ch10
#4.
#import datetime as dt
dates = [dt.datetime(2015,1,13)+dt.timedelta(i) for i in range(5)]
closes = [7.31,7.28,7.40,7.43,7.41]
prices = {dates[i]:closes[i] for i in range(5)}
prices[dt.datetime(2015,1,20)] = 7.44
dates.append(dt.datetime(2015,1,20))
prices[dt.datetime(2015,1,21)- dt.timedelta(4)]
prices[dt.datetime(2015,1,16)] = 7.50

#5.
import math
cash = 10000
share = {dates[0]:0}
for i in range(1,6):
    if prices[dates[i]]>prices[dates[i-1]]:
        buyshare = math.floor(0.5*cash/prices[dates[i]])
        share[dates[i]]= buyshare
        cash=cash-buyshare*prices[dates[i]]+share[dates[i-1]]*prices[dates[i]]
    else:
         share[dates[i]]= 0


share


Ch11
#4.
sample = np.array([0.5,1.43,-1.36,-0.16,0.29,-0.59,
	              1.16,-0.33,0.07,-1.36])

np.mean(sample)
np.var(sample)
np.std(sample)
np.median(sample)