import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(('degree','minute','second','radius'))

vals['de'] = vals['degree'] + (vals['minute']/60) + (vals['second']/3600)
vals['ra'] = vals['de']/180
vals['rap'] = vals['ra']*math.pi
vals['len'] = vals['radius']*vals['r']
vals['lenp'] = vals['rap']*vals['r']

print('')
print(prettyFunction("{degree!}{degree}{minute!}\"{second!}\' = {de!}{degree} = {ra!}{pi}", vals))
print(prettyFunction("Arc length = {ra!}{pi} x {radius!} = {len!}{pi}", vals))
print(prettyFunction("{len!}{pi} {approx} {lenp!}", vals))
