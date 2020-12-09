#'''Checking the weather seems fairly trivial: Open your web browser, click the
# address bar, type the URL to a weather website (or search for one and then
# click the link), wait for the page to load, look past all the ads, and so on.
# Actually, there are a lot of boring steps you could skip if you had a program that downloaded the weather forecast for the next few days and printed
# it as plaintext. This program uses the requests module from Chapter 11 to
# download data from the Web.
# Overall, the program does the following:
#•	 Reads the requested location from the command line.
#•	 Downloads JSON weather data from OpenWeatherMap.org.
#•	 Converts the string of JSON data to a Python data structure.
#•	 Prints the weather for today and the next two days.
#So the code will need to do the following:
#•	 Join strings in sys.argv to get the location.
#•	 Call requests.get() to download the weather data.
#•	 Call json.loads() to convert the JSON data to a Python data structure.
#•	 Print the weather forecast. '''

#  Step 1: Get Location from the Command Line Argument
#  The input for this program will come from the command line. 


import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
 print('Usage: quickWeather.py location')
 sys.exit()
location = ' '.join(sys.argv[1:])

#  Step 2: Download the JSON Data
# OpenWeatherMap.org provides real-time weather information in

#  JSON format. Your program simply has to download the page at

# http://api.openweathermap.org/data/2.5/forecast/daily?q=<Location>&cnt=3,

#  where <Location> is the name of the city whose weather you want. Add
 
# the following to quickWeather.py.


# Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

''' We have location from our command line arguments. To make the URL
we want to access, we use the %s placeholder and insert whatever string is
stored in location into that spot in the URL string. We store the result in
url and pass url to requests.get(). The requests.get() call returns a Response
object, which you can check for errors by calling raise_for_status(). If no
exception is raised, the downloaded text will be in response.text.  '''


#  Step 3: Load JSON Data and Print Weather

'''  The response.text member variable holds a large string of JSON-formatted
data. To convert this to a Python value, call the json.loads() function.  '''

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
#  visit the online documentation to see which key value corresrponds to the data that you need
#  Print weather descriptions
w = weatherData['list']

print('Current weather in %s:' % (location))


# Current weather in San Francisco, CA:
# Clear - sky is clear
 
# Tomorrow:
# Clouds - few clouds

Day after tomorrow:
Clear - sky is clear
