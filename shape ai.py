import requests
import sys

from datetime import datetime

api_key = '7329e44641f618803d732a33a4f1d60d'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

def printoutput():
    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("-------------------------------------------------------------")

    print ("Current temperature is: {:.2f} deg C".format(temp_city))
    print ("Current weather desc  :",weather_desc)
    print ("Current Humidity      :",hmdt, '%')
    print ("Current wind speed    :",wind_spd ,'kmph')

printoutput()

sys.stdout = open('shapeai.txt', 'w')
print(printoutput())
sys.stdout.close()

#x=open('shapeai.txt','a')
#print('{}' (printoutput()), file=x)
#x.close()

#with open('shapeai.txt','w')as x:
  #  x_contents = x.write()
  #  print(x_contents)





