API_KEY = "d5fb21995d2169b59b565c4a16ae7349"
LATITUDE = "41.786"
LONGITUDE = "-87.752"

# April 18th 2017 at 12:00:00am
FIRST_DATE = 1492475200

# Aug 17 11pm
LAST_DATE = 1503702000
DAY = 86400


API_LINK = "https://api.darksky.net/forecast/{0}/{1},{2}".format(API_KEY, LATITUDE, LONGITUDE)

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

QUERY = "INSERT INTO  darksky_weather (timestamp, temperature, pressure, wind_speed, wind_direction, humidity, precipitation, uv_index) VALUES "
