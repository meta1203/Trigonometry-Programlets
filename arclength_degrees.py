import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(('d','r'))

vals['ra'] = vals['d']/180
vals['rap'] = vals['ra']*math.pi
vals['len'] = vals['ra']*vals['r']
vals['lenp'] = vals['rap']*vals['r']

print('')
print(prettyFunction("Arc Length = ({d!}{degrees} x {pi} / 180) x {r!}", vals))
print(prettyFunction("{len!}{pi} = {ra!}{pi} x {r!}", vals))
print(prettyFunction("{len!}{pi} {approx} {lenp!}", vals))
