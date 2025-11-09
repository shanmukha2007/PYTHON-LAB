import jso
weather_json = '''
{
  "city": "Chennai",
  "current": {"temp": 42, "humidity": 70},
  "forecast": [
    {"day": "Mon", "condition": "Rain", "temp": 34},
    {"day": "Tue", "condition": "Sunny", "temp": 36},
    {"day": "Wed", "condition": "Rain", "temp": 32}
  ]
}
''’
data = json.loads(weather_json)
if data["current"]["temp"] > 40:
    print("ALERT: High temperature!")
