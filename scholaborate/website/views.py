from django.shortcuts import render
from django.conf import settings
import requests, json, googlemaps

def home(request):
	return render(request, "shopping_home.html", {'STATIC_URL':settings.STATIC_URL})

def profile(request):
	send_url = 'http://freegeoip.net/json'
	r = requests.get(send_url)
	j = json.loads(r.text)
	lat = j['latitude']
	lng = j['longitude']

	link = "https://maps.googleapis.com/maps/api/geocode/"\
	 + "json?latlng=%s,%s&key=%s" % (lat, lng, settings.GOOGLE_MAPS_API_KEY)
	address = json.loads(requests.get(link).text)
	place = ""
	for component in address['results'][0]['address_components']:
		place += component['short_name'] + " "

	return render(request, "shopping_profile.html",
		{
			'STATIC_URL':settings.STATIC_URL,
			'current_location': place,
		})