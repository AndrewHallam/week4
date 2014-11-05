### "save"
import matplotlib
from visualise import show_green_in_png
from URL import map_at
from pnggreen import count_green_in_png
from geolocation import geolocate
from points import location_sequence
import numpy as np

matplotlib.use('Agg')

def plotgreengraph(city1, city2):
   import matplotlib.pyplot as plt 
   loca1=geolocate(city1)
   loca2=geolocate(city2)
   centre=np.mean(np.array([loca1, loca2]), axis=0)
   
   with open('green_{}_{}.png'.format(city1,city2),'w') as green:
      green.write(show_green_in_png(map_at(centre[0],centre[1],
        zoom=10,satellite=True)))
             
   plt.plot([
   count_green_in_png(
        map_at(*location,zoom=10,satellite=True))
          for location in location_sequence(
              geolocate(city1),
              geolocate(city2),10)])
   plt.savefig('greengraph_{}_{}.png'.format(city1,city2))   
         
#print london_location

#map_response=map_at(51.5072, -0.1275, zoom=10)
#url=map_response.url
#print url

#print count_green_in_png(map_at(*london_location))

#[count_green_in_png(map_at(*location,zoom=10,satellite=True))
#            for location in location_sequence(
#                geolocate("London"),
#                geolocate("Birmingham"),
#                10)]

#matplotlib.use('Agg')
        
#with open('green.png','w') as green:
#    green.write(show_green_in_png(map_at(*london_location,
#        zoom=10,satellite=True)))

#plt.plot([
#    count_green_in_png(
#        map_at(*location,zoom=10,satellite=True))
#          for location in location_sequence(
#              geolocate("London"),
#              geolocate("Birmingham"),10)])
#plt.savefig('greengraph.png')