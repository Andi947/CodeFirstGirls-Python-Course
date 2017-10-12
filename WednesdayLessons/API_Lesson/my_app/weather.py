import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"fe7484e6b582838b04398c9b7da8f6af"}

response = requests.get(endpoint, params=payload)
data = response.json()

print data["main"]
print response.url
print response.status_code
print response.headers["content-type"]
print
print "This is the unprocessed weather: "
print
print response.text

print

print "This is the processed weather: "
print
temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print u"It's {}C in {}, and the sky is {}".format(temperature, name, weather)

#json formatter - online
