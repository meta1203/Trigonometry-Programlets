# Calculate length of an arc using radius and radian angle measurement
import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(('radians','radius'))

# Calculate arc length
vals['len'] = vals['radians']*vals['radius']
# Calculations with pi
vals['lenp'] = vals['rap']*vals['radius']
vals['rap'] = vals['radians']*math.pi

print('')
print(prettyFunction("{len}{pi} = {radians}{pi} x {radius}", vals))
print(prettyFunction("{len}{pi} {approx} {lenp}", vals))
