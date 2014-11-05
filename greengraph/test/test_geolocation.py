from ..geolocation import geolocate
from nose.tools import assert_raises, assert_almost_equal

# Test whether a nonstring raises an error.
def test_nonstring():
   with assert_raises(TypeError) as exception: geolocate([])

# Test whether a string which doesn't exist raises an error.

def test_nowhere():
   with assert_raises(TypeError) as exception: geolocate("adscb1245da")

# Test geolocation gives the coordinate location by comparing with google.

def test_location():
  loc_warr=geolocate("Warrington")
  assert_almost_equal(loc_warr[0], 53.3900441, places=2)
  assert_almost_equal(loc_warr[1], -2.5969501, places=2)