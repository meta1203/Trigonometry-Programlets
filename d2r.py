import math
from stdutils import prettyFunction, inputAsDict

vals = inputAsDict(["degrees"])

vals['rad'] = vals['degrees']/180
vals['radp'] = vals['rad']*math.pi
vals['floatDegrees'] = vals['degrees']

print('')
print(prettyFunction("{floatDegrees}{degree} = {rad}{pi} {approx} {radp}",vals))
