import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config

owm = OWM('939fd8833ea7f0c9c1f0a95d088a527a')
mgr = owm.weather_manager()

info = input('What information are you interested in? (temperature-0, fall-out-1, all-2): ')

place = input('What city are you interested in?: ')

config_dict = get_default_config()
config_dict['language'] = 'en'


observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]


if info == '0':
    print('The temperature is now in the area ' + str(temp) + " degrees Celsius")
if info == '1':
    print('In the city  ' + place + " now " + w.detailed_status)
if info == '2':
    print('In the city ' + place + " now " + w.detailed_status)
    print('The temperature is now in the area ' + str(temp) + " degrees Celsius")

input('Press ENTER to Exit')
 


