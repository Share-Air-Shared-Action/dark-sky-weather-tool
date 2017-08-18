# dark-sky-weather-tool
This weather tool will use python to download hourly forecasts and upload it to a PostgreSQL
1) Temperature (F) 
2) Barometric Pressure
3)      Wind Speed (WS)
4)      Wind Direction (WD)  please note that this is a vector  thus, the data cannot be mathematically averaged. We need 1-hour WD and WS data to create the wind-rose during the community air monitoring in each community
5)      Relative Humidity: between 0 and 1
6)      Water vapor pressure
7)      Precipitation
8)      Solar Radiation.

41.786,-87.752
  https://api.darksky.net/forecast/3d5abd0dd03dc038cc654a14255173cb/41.786,-087.752,1500240486
