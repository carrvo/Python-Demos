import __vars__
__vars__.__choice__ = 'that'
from test import shared
print(shared('me'))
assert shared('me') == 'that me'
