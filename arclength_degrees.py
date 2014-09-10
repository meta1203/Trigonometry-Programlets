# Calculate length of an arc using radius and degree angle measurement

import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(('d','r'))

# Convert degrees to radians
vals['ra'] = vals['d']/180
# Calculate arc length
vals['len'] = vals['ra']*vals['r']
# Calculations with pi
vals['rap'] = vals['ra']*math.pi
vals['lenp'] = vals['rap']*vals['r']

# Print out values
print('')
print(prettyFunction("Arc Length = ({d!}{degree} x {pi}/180) x {r!}", vals))
print(prettyFunction("{len!}{pi} = {ra!}{pi} x {r!}", vals))
print(prettyFunction("{len!}{pi} {approx} {lenp!}", vals))
