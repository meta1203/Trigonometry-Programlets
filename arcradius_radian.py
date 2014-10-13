import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(('radians','arc'))

vals['rap'] = vals['radians']*math.pi
vals['len'] = vals['arc']/vals['ra']
vals['lenp'] = vals['arc']/vals['rap']

print('')
print(prettyFunction("Radius = {arc}/{radians}{pi} = {len}/{pi}", vals))
print(prettyFunction("{len}/{pi} {approx} {lenp}", vals))
