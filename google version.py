import pprint
import googlemaps
import time
from geopy.geocoders import Nominatim
import random
api_key = "enter api key here"
gmaps = googlemaps.Client(key = api_key)

address = input("What is your city ")
user_request = input('Do you have any ideas (i.e Italian) ')
geolocator = Nominatim(user_agent="Goose")
location = geolocator.geocode(address)
latlong = str(location.latitude) + ',' + str(location.longitude)
if not user_request == "":
    places_result = gmaps.places_nearby(location=latlong, radius=16093, open_now=True, type='meal_delivery',keyword=user_request)
else:
    places_result = gmaps.places_nearby(location=latlong, radius=16093, open_now=True, type='meal_delivery', )
roll_again = 'yes'
while roll_again == 'yes':
    print(len(places_result))
    ran_num = random.randint(0, len(places_result))
    print('Eat at ' + str(places_result['results'][ran_num]['name']))
    roll_again = input('Would you like to roll again? (type yes if so) ')