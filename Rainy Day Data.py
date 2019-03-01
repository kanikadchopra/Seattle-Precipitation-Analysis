import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

# Extracting the data from a CSV file using pandas
rainfall = pd.read_csv('seattle_raindata.csv')['PRCP'].values

# Rainfall is in mm, so we have to conert it to inches
inches = rainfall/254.0
inches.shape # shows that it is 365 days 

# We have the daily rainfall in inches now from January 1 to December 31 for  
# the year 2014

# Extra questions:
# 1. How many rain days were there in the year? How many days without rain 
# were there?
rainy = (inches > 0) 
print("Number of days without rain:", np.sum(inches==0))
print("Number of days with rain:", np.sum(rainy))

# 2. What is the average precipitation on those rainy days?
avg_rain = np.average(inches[inches!=0])
print("The average precipitation on rainy days is:", avg_rain)

# 3. How many days were there with more than half an inch of rain?
print("Days with more than 0.5 inches of rain:", np.sum(inches>0.5))

# 4. Number of days with less than 0.2 inches of rain?
print("Days with < 0.2 inches of rain:", np.sum((inches<0.2)& (inches>0)))

# 5. Monthly breakdown
rain_dates = pd.read_csv('seattle_raindata.csv', usecols=[2,3])
rain_dates['PRCP'] = rain_dates['PRCP']/254.0

def month_lst_creator(info):
    month_lst = []
    day_lst =[]
    for i in range(len(info)):
        date = str(info['DATE'][i])
        month = date[4:6]
        day = date[-2:]
        month_lst = month_lst + [month]
        day_lst = day_lst + [day]
    return month_lst, day_lst
        
rain_dates['Year'] =2014
rain_dates['Month'] = month_lst_creator(rain_dates)[0]
rain_dates['Day'] = month_lst_creator(rain_dates)[1]

# Calculating the monthly average for each month
# Given a month as a string, e.g. '01', it calculates the average precipitation
def average_month(month):
    return np.average(rain_dates[rain_dates['Month'] == month]['PRCP'])

# Creates a dictionary that calculates the average precipitation for each month
# and stores it in dic
    
def average_rain_dic():
    dic = {}
    for i in range(1,13):
        month = str(i)
        if len(month) == 1:
            month = '0' + month
            dic[month] = average_month(month)
        else:
            dic[month] = average_month(month)
    return dic

monthly_average = pd.Series(average_rain_dic())
month_names=['Jan', 'Feb', 'Mar', 
                            'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 
                            'Nov', 'Dec']

## Plot the monthly average on a histogram:
monthly_average.plot.bar()
plt.xlabel('Months')
plt.ylabel("Amount of precipitation (inches)")
plt.title("Monthly Average Precipitation")

# 6. What day had the most/least rain? (Not including dates with no rain)
max_rain = np.max(rain_dates['PRCP'])
max_rain_month = rain_dates[rain_dates['PRCP'] == max_rain]['Month'].to_string(
        index=False)
max_rain_day = rain_dates[rain_dates['PRCP'] == max_rain]['Day'].to_string(
        index=False)
rain_dates[rain_dates['PRCP'] == max_rain]
print('\n')
print("The most amount of rain was", max_rain, "inches and occured on", 
      max_rain_month + "/" + max_rain_day + '/2014')

all_rain = inches[inches!=0] # all days with rain 
min_rain = np.min(all_rain)

# This function takes the dates that have the least amount of rain and creates 
# a string that is printable

def min_rain_dates(info):
    date_str = ""
    for i in range(len(info)):
        data = info.iloc[i]
        month = info.iloc[i]['Month']
        day = info.iloc[i]['Day']
        new_date = month + '/' + day + '/2014'
        date_str = date_str + ',' + new_date
        
    return date_str

min_rain_data = rain_dates[rain_dates['PRCP']==min_rain] # All dates with min rain
min_rain_dates_lst = min_rain_dates(min_rain_data)[1:]
print('\n')
print("The least amount of rain was", min_rain, "inches and occured on the dates:",
      min_rain_dates_lst)

# 7. Overall Summary statistics for rain in a DataFrame
dic = {'minimum rain (inches)': min_rain, 'maximum rain (inches)': max_rain, 
       'average rain (inches)': avg_rain,
       'days with rain': np.sum(inches!=0), 'days without rain': np.sum(
               inches==0), 'median precip on rainy days (inches)': np.median(inches[rainy])}
summary_stats = pd.Series(dic)
print('\n')
print("The summary statistics for rainfall in Seattle in 2014 are:")
print(summary_stats)

# 8. Seasonal analysis on the rain
# Summer: June 21 to Sept 22
# Spring: Mar 31 to June 20
# Winter: Jan 1 to March 20, and Dec 21 to Dec 31
# Fall: Sept 23 to Dec 20

days = np.arange(365)
summer = (days > 172) & (days < 265)
spring = (days > 80) & (days <171)
fall = (days >264) & (days <354)
winter = ((days > 1 ) & (days<79)) | ((days>355) & (days<364))

season_average = {"Summer": np.average(inches[rainy & summer]),
                  "Spring": np.average(inches[rainy & spring]),
                  "Fall": np.average(inches[rainy & fall]), 
                  "Winter": np.average(inches[rainy & winter])}
                  
season_maximums = {"Summer": np.max(inches[rainy&summer]), 
                   "Spring": np.max(inches[rainy&spring]),
                   "Fall": np.max(inches[rainy&fall]), 
                   "Winter":np.max(inches[rainy&winter])}
season_maximums_data = pd.Series(season_maximums)
season_average_data = pd.Series(season_average)

# Printing out all the data calculated
print('\n')
print("Seasonal Data:")
print("Here are the season's average precipitation:")
print(season_average_data)
print('\n')
print("Here are the season's maximum precipitation:")
print(season_maximums_data)
