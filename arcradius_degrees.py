import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(('degree','arc'))

vals['ra'] = vals['degree']/180
vals['rap'] = vals['ra']*math.pi
vals['len'] = vals['arc']/vals['ra']
vals['lenp'] = vals['arc']/vals['rap']

print('')
print(prettyFunction("Radius = {arc}/({degree}{degree} x {pi} / 180)", vals))
print(prettyFunction("Radius = {arc}/{ra}{pi} = {len}/{pi}", vals))
print(prettyFunction("{len}/{pi} {approx} {lenp}", vals))
