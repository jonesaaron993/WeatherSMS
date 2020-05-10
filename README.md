# WeatherSMS
Sends weather data via SMS

In order to send SMS messages, I use the service Twilio.
![Image of Twilio](https://www.twilio.com/marketing/bundles/company-brand/img/logos/red/twilio-logo-red.png)

I followed this tutorial, but altered some formatting and functions they used.

https://www.twilio.com/blog/2016/04/how-to-send-a-text-message-with-python.html

**IMPORTANT:** Initially Twilio is free, but eventually you will have to pay for their service. I run this python script once a day to give me the weather in my area, which amounts to 0.01 per SMS.

To get the weather for my location, I used [pyowm](https://github.com/csparpa/pyowm), which is a wrapper of [OpenWeatherMap](https://openweathermap.org/)

Pyowm             |  OpenWeatherMap
:-------------------------:|:-------------------------:
![](https://pyowm.readthedocs.io/en/latest/_images/180x180.png)  |  ![](https://openweathermap.org/themes/openweathermap/assets/img/openweather-negative-logo-RGB.png)

Just change the following lines to your own versions and you should be up and running.

```
#Twilio settings
account = 'ACCOUNT ID'
token = 'TOKEN ID'

#API key for pyowm
owm = pyowm.OWM('API KEY')

#Get location data for the relevent area
observation = owm.weather_at_place('CITY,COUNTRY')
```

And the message function
```
#Send Message
client.messages.create(from_='TWILIO NUMBER', to='YOUR NUMBER', 
    body=finalMessage)
```
