### "save"
import matplotlib
from visualise import show_green_in_png
from URL import map_at
from pnggreen import count_green_in_png
from geolocation import geolocate
from points import location_sequence

london_location=geolocate("London")
print london_location

map_response=map_at(51.5072, -0.1275, zoom=10)
url=map_response.url
print url

print count_green_in_png(map_at(*london_location))

[count_green_in_png(map_at(*location,zoom=10,satellite=True))
            for location in location_sequence(
                geolocate("London"),
                geolocate("Birmingham"),
                10)]

matplotlib.use('Agg')
import matplotlib.pyplot as plt

#open('asdf.png','w').write(
#    show_green_in_png(
#        map_at(*london_location,
#        zoom=10,satellite=True)
#    )
#    )
        
with open('green.png','w') as green:
    green.write(show_green_in_png(map_at(*london_location,
        zoom=10,satellite=True)))

plt.plot([
    count_green_in_png(
        map_at(*location,zoom=10,satellite=True))
          for location in location_sequence(
              geolocate("London"),
              geolocate("Birmingham"),10)])
plt.savefig('greengraph.png')