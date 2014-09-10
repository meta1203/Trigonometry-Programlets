import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(('d','arc'))

vals['ra'] = vals['d']/180
vals['rap'] = vals['ra']*math.pi
vals['len'] = vals['arc']/vals['ra']
vals['lenp'] = vals['arc']/vals['rap']

print('')
print(prettyFunction("Radius = {arc!}/({d!}{degrees} x {pi} / 180)", vals))
print(prettyFunction("Radius = {arc!}/{ra!}{pi} = {len!}/{pi}", vals))
print(prettyFunction("{len!}/{pi} {approx} {lenp!}", vals))
