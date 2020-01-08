from collections import namedtuple
import requests
import sys


#osoba = namedtuple("osoba", ['imie', 'wiek'])

#os1 = osoba(imie='Wojtek', wiek=39)

#print(os1)

#url = "https://www.metaweather.com/api/location/search/?query=london"

#r = requests.get(url)
#json_data = json.loads(r.text)
#for i in json_data:
#    print(i)

#weather = json_data[0]
#print(weather.get("woeid"))


Weather = namedtuple("Weather", ['location_name', 'the_temp', 'air_pressure', 'humidity'])


def get_locatrion_id(location_id):
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={location_id}")
    return resp.json()[0]["woeid"]


def get_location_weather(location_id):
    resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    location = resp.json()['title']
    curr_data = resp.json()["consolidated_weather"][0]
    weather = Weather(location_name=location, the_temp=curr_data['the_temp'], air_pressure=curr_data['air_pressure'],
                      humidity=curr_data['humidity'])
    return weather


def weather_report(weather):
    report = f"""Pogoda w {weather.location_name}
temperatura: {weather.the_temp}
wilgotnosc: {weather.humidity}
cisnienie: {weather.air_pressure}
"""
    return report


if __name__ == "__main__":
    try:
        location_name = sys.argv[1]
        location_id = get_locatrion_id(location_name)
        weather = get_location_weather(location_id)
        report = weather_report(weather)
        print(report)
    except IndexError:
        print("podaj nazwe lokalizacji")




