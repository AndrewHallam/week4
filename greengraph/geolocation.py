### Geolocation will find the location of a string using Google Maps. 
import geopy
geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
def geolocate(place):
  geo1=geocoder.geocode(place,exactly_one=False)
  if geo1 is None:
     raise TypeError("This is not a location")
  return geocoder.geocode(place,exactly_one=False)[0][1]
