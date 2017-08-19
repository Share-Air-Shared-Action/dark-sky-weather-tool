from requests import get
from constants import *
from datetime import datetime, timedelta
import psycopg2
from json import dump

# Connect to database
conn = psycopg2.connect("dbname='sasa-airquality' user='postgres'")

cur = conn.cursor()

yesterday = (datetime.now() - timedelta(days=1)).isoformat()
# print(data.json())

#First time usage only
date = FIRST_DATE
query = QUERY
while(date <= yesterday):
    #renew API Link to ask for information
    api_link = "{0},{1}".format(API_LINK,date)

    #HTTP GET Request that returns a json dict
    result = get(api_link)
    data = result.json()
    hour = 0 
    val = []
    for hour in range(24):
        hourly = data[HOURLY][DATA][HOUR] 
        val.extend([hourly[TIMESTAMP], hourly[TEMP], hourly[PRESSURE]])
        val.extend([hourly[WIND_SPEED], hourly[WIND_DIRECTION], hourly[HUMIDITY]])
        val.extend([hourly[PRECIPITATION], hourly[UV_INDEX]])

        if date >= LAST_DATE:
            query += "(val[:]);"
        else:
            query+="(val[:]), "
    
    date += DAY

cur.execute(query)
#Loop to create string
#print(weather) 
#def first_time():
##
#    date = FIRST_DATE
#    yesterday = (datetime.now() - timedelta(days=1)).isoformat()
#    weather = forecast(*CHICAGO, time=yesterday)
#    print(weather) 
##    while date <= yesterday:
#        weather = forecast(*CHICAGO, time=yesterday)
#        print(weather) 
#        date = date + DAY
