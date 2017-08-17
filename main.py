from darksky import forecast
from constants import *
from datetime import datetime, timedelta


date = FIRST_DATE
yesterday = (datetime.now() - timedelta(days=1)).isoformat()
weather = forecast(*CHICAGO, time=yesterday)
    print(weather) 
def main():
    print("hello")
    first_time()


def first_time():

    date = FIRST_DATE
    yesterday = (datetime.now() - timedelta(days=1)).isoformat()
    weather = forecast(*CHICAGO, time=yesterday)
    print(weather) 
#    while date <= yesterday:
#        weather = forecast(*CHICAGO, time=yesterday)
#        print(weather) 
#        date = date + DAY
