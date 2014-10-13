import math
from stdutils import prettyFunction, inputAsDict

print("y = ax^2 + bx + c")
vals = inputAsDict(('a','b','c'))

calcs = {'x1': (-vals['b'] + math.sqrt(vals['b']**2 - 4*vals['a']*vals['c']))/(2*vals['a']), 'x2': (-vals['b'] - math.sqrt(vals['b']**2 - 4*vals['a']*vals['c']))/(2*vals['a'])}

print(prettyFunction("({x1},0),({x2},0)", calcs))
