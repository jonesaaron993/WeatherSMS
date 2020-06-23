# WeatherSMS
Sends weather data via SMS

In order to send SMS messages, I use the service Twilio.
![Image of Twilio](https://cdn.statically.io/img/s8754.pcdn.co/wp-content/uploads/edd/2017/08/twilio-ninja-forms-logo.png?quality=70)

I followed this tutorial, but altered some formatting and functions they used.

https://www.twilio.com/blog/2016/04/how-to-send-a-text-message-with-python.html

**IMPORTANT:** Initially Twilio is free, but eventually you will have to pay for their service. I run this python script once a day to give me the weather in my area, which amounts to 0.01&#65504; per SMS. Since Twilio gives you around $15 of free starting cash, you can send about 150,000 SMS if you only send one per day.

To get the weather for my location, I used [pyowm](https://github.com/csparpa/pyowm), which is a wrapper of [OpenWeatherMap](https://openweathermap.org/).

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

#Get location data for the relevant area
observation = owm.weather_at_place('CITY,COUNTRY')
```
**IMPORTANT:** Make sure to format your country in the `COUNTRY` tag to your country's abbreviations. I.e, if you are in the United States, format it to `US`.

And the message function.
```
#Send Message
client.messages.create(from_='TWILIO NUMBER', to='YOUR NUMBER', 
    body=finalMessage)
```
