import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import Quandl as q #imports Quandl and assigns 'q' as its shortcut so we can just type q.get() etc
import os

vix = q.get("YAHOO/INDEX_VIX")
#vixmonthly = q.get("YAHOO/INDEX_VIX", collapse="monthly")
#allhilows = vixdata.loc[:,['High', 'Low']]

#path = os.path.expanduser('~/vix-analysis/monthly.xlsx')
#vix2 = pd.read_excel('monthly.xlsx')


#leap years: 1992, 1996, 2000, 2004, 2008, 2012

monthlim = {1: 31 , 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
indextomonth = {1: 'January',
		   2: 'February',
		   3: 'March',
		   4: 'April',
		   5: 'May',
		   6: 'June',
		   7: 'July',
		   8: 'August',
		   9: 'September',
		   10: 'October',
		   11: 'November',
		   12: 'December'}

def printextrema(startyear, endyear):

	# for curyear in range(startyear, endyear + 1):
	# 	for curmonth in range(0, 12):
	# 		for curday in range(0, monthlim[curmonth + 1]): #find lowest low & highest high of each month
	# 			try:
	# 				lowval = 999
	# 				highval = 0
	# 				if curday == 0:
	# 					lowval = vix.loc['%d-%d-%d' % (curyear, curmonth + 1, curday + 1),'Low']
	# 					highval = vix.loc['%d-%d-%d' % (curyear, curmonth + 1, curday + 1),'High']
	# 				else:
	# 					nextlow = vix.loc['%d-%d-%d' % (curyear, curmonth + 1, curday + 1),'Low']
	# 					nexthigh = vix.loc['%d-%d-%d' % (curyear, curmonth + 1, curday + 1),'High']				
	# 					if nextlow < lowval:
	# 						lowdate = '%d-%d-%d' % (curyear, curmonth + 1, curday + 1)
	# 						lowval = nextlow
	# 					if nexthigh > highval:
	# 						highdate = '%d-%d-%d' % (curyear, curmonth + 1, curday + 1)
	# 						highval = nexthigh
	# 			except KeyError:
	# 				hi = 1
	# 		print('Lowest Low for %s: %d' % (lowdate, lowval))
	# 		print('Highest High for %s: %d' % (highdate, highval))
	# 		print()


	lowdate = ''
	highdate = ''
	curlow = np.nan
	curhigh = np.nan
	for year in range(startyear, endyear):
		for month in range(12):
			for day in range(monthlim[month + 1]):
				if year == startyear:
					day += 1
					curlow = 999
					curhigh = 0
				curdatestr = '%d-%d-%d' % (year, month + 1, day + 1)
				lastopen = vix.index.asof(curdatestr)
				curdate = pd.to_datetime(curdatestr)

				if curdate.is_month_start == True:
					curlow = 999
					curhigh = 0
				nextlow = vix.loc[lastopen, 'Low']
				nexthigh = vix.loc[lastopen, 'High']
				if nextlow < curlow:
					lowdate = curdate
					curlow = nextlow
				if nexthigh > curhigh:
					highdate = curdate
					curhigh = nexthigh
				if curdate.is_month_end:
					break
			print('_______________________________________')
			print()
			print('Extrema for %s, %d:' % (indextomonth[month + 1], year))
			print()
			print('Lowest Low: $%d on %s %d' % (curlow, indextomonth[lowdate.month], lowdate.day))
			print('Highest High: $%d on %s %d' %  (curhigh, indextomonth[highdate.month], highdate.day))
			print(month)
			print('_______________________________________')
			#date_range


		
printextrema(1990, 2015)

#s.to_frame(name='column_name').to_excel('xlfile.xlsx', sheet_name='s')

