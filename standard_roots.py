import math
from stdutils import prettyFunction, inputAsDict

print("y = a(x - h)^2 + k")
vals = inputAsDict(('a','h','k'))
a = vals['a']
b = -(vals['h']*2*a)
c = (vals['k']*4*a+b**2)/(4*a)

calcs = {'x2': (-b + math.sqrt(b**2 - 4*a*c))/(2*a), 'x1': (-b - math.sqrt(b**2 - 4*a*c))/(2*a)}

print(prettyFunction("({x1},0),({x2},0)", calcs))
