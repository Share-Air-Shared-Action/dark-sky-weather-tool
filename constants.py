
API_KEY = "3d5abd0dd03dc038cc654a14255173cb"
LATITUDE = "41.786"
LONGITUDE = "-87.752"

# April 18th 2017 at 12:00:00am
FIRST_DATE = 1492475200
LAST_DATE = 1502989200 
DAY = 86400


API_LINK = "https://api.darksky.net/forecast/{0}/{1},{2}".format(API_KEY,LATITUDE,LONGITUDE)

HOURLY = "hourly"
DATA = "data"

TIMESTAMP = "time"
TEMP = "temperature"
PRESSURE = "pressure"
WIND_SPEED = "windSpeed"
WIND_DIRECTION = "windBearing"
HUMIDITY = "humidity"
PRECIPITATION = "precipIntensity"
UV_INDEX = "uvIndex"

QUERY = "INSERT INTO  darksky-weather VALUES "
