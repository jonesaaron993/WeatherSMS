import pyowm, json
from twilio.rest import Client

#Twilio settings
account = 'ACCOUNT ID'
token = 'TOKEN ID'

#API key for pyowm
owm = pyowm.OWM('API KEY')

#Get location data for the relevent area
observation = owm.weather_at_place('CITY,COUNTRY')

#Store relevent data from the declared place
w = observation.get_weather()

#Weather details
wind = w.get_wind()
temp = w.get_temperature('fahrenheit')

#Dump and load json string
windDump = json.dumps(wind)
windLoad = json.loads(windDump)

#Store speed number
speed = windLoad["speed"]

#Dump and load jason string
tempDump = json.dumps(temp)
tempLoad = json.loads(tempDump)

#Store final, max, and min temp
tempFinal = tempLoad["temp"]
tempMax = tempLoad["temp_max"]
tempMin = tempLoad["temp_min"]

#Create the final message to display
finalMessage = ("Weather for CITY" 
    + "\n\nCurrent Temp: " + str(tempFinal) 
    + "\n\nMax Temp: " + str(tempMax) 
    + "\n\nMin Temp: " + str(tempMin) 
    + "\n\nWind Speed: " + str(speed))

#Use twilio client
client = Client(account, token)

#Send Message
client.messages.create(from_='TWILIO NUMBER', to='YOUR NUMBER', 
    body=finalMessage)