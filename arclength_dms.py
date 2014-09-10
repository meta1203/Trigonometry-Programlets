# Calculate length of an arc using radius and Degrees Minutes and Seconds angle measurement

import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(('degree','minute','second','radius'))

# Convert DMS to radians
vals['de'] = vals['degree'] + (vals['minute']/60) + (vals['second']/3600)
vals['ra'] = vals['de']/180
# Calculate arc length
vals['len'] = vals['radius']*vals['r']
# Calculations with pi
vals['rap'] = vals['ra']*math.pi
vals['lenp'] = vals['rap']*vals['r']

# Print out values
print('')
print(prettyFunction("{degree!}{degree}{minute!}\"{second!}\' = {de!}{degree} = {ra!}{pi}", vals))
print(prettyFunction("Arc length = {ra!}{pi} x {radius!} = {len!}{pi}", vals))
print(prettyFunction("{len!}{pi} {approx} {lenp!}", vals))
