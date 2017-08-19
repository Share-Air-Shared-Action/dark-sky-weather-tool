from requests import get
from constants import *
from datetime import datetime, timedelta
import psycopg2
from json import dump

# Connect to database
conn = psycopg2.connect("dbname='sasa_airquality' user='postgres'")

cur = conn.cursor()

yesterday = int((datetime.now() - timedelta(days=1)).strftime('%s'))
# print(data.json())

#First time usage only
date = FIRST_DATE
query = QUERY
while(date <= LAST_DATE):
    #renew API Link to ask for information
    api_link = "{0},{1}".format(API_LINK,date) 
    #HTTP GET Request that returns a json dict
    result = get(api_link)
    data = result.json()
    hour = 0 
    for hour in range(24):
        val = []
        hourly = data[HOURLY][DATA][hour] 
        val.extend([hourly[TIMESTAMP]])

        for col in COLUMNS:
            if col in hourly.keys():
                if col == "humidity":
                    val.extend([int(hourly[col]*100)])
                else:
                    val.extend([hourly[col]])
            else:
                val.extend([-1])

  #       print(val, len(val)) 

        if date >= LAST_DATE:
            query += "({0});".format(val[:])
        else:
            query+="({0}), ".format(val[:])
    
    date += DAY
    
print(query)
#cur.execute(query)

