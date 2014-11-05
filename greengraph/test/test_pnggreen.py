from ..pnggreen import is_green
from  nose.tools import assert_false

# Check that is_green has a reasonable definition of green
def test_green():
   assert(is_green(1,10,1))
   assert_false(is_green(10,1,10))