API_KEY = "f3d8f5f8a80ab50c23e1ddc85f6ba25c"
LATITUDE = "41.786"
LONGITUDE = "-87.752"

# April 18th 2017 at 12:00:00am
FIRST_DATE = 1492475200

# Aug 17 11pm
LAST_DATE = 1503115200
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
COLUMNS = [TEMP, PRESSURE, WIND_SPEED, WIND_DIRECTION, HUMIDITY, PRECIPITATION, UV_INDEX]

QUERY = "INSERT INTO  darksky-weather VALUES "
