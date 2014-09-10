import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(('radians','radius'))

vals['rap'] = vals['radians']*math.pi
vals['len'] = vals['radians']*vals['radius']
vals['lenp'] = vals['rap']*vals['radius']

print('')
print(prettyFunction("{len!}{pi} = {radians!}{pi} x {radius!}", vals))
print(prettyFunction("{len!}{pi} {approx} {lenp!}", vals))
