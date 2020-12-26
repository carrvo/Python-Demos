import __vars__
__vars__.__choice__ = 'this'
from test import shared
print(shared('me'))
assert shared('me') == 'this me'
