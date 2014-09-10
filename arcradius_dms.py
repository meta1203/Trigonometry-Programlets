import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(('degree','minute','second','arc'))

vals['de'] = vals['degree'] + (vals['minute']/60) + (vals['second']/3600)
vals['ra'] = vals['de']/180
vals['rap'] = vals['ra']*math.pi
vals['len'] = vals['arc']/vals['ra']
vals['lenp'] = vals['arc']/vals['rap']

print('')
print(prettyFunction("{degree!}{degree}{minute!}\"{second!}\' = {de!}{degree} = {ra!}{pi}", vals))
print(prettyFunction("Radius = {arc!}/{ra!}{pi} = {len!}/{pi}", vals))
print(prettyFunction("{len!}/{pi} {approx} {lenp}", vals))
