import math
from stdutils import inputAsDict, prettyFloat

vals = inputAsDict(('x1','y1','x2','y2'))

print(prettyFloat(math.sqrt((vals['y2']-vals['y1'])**2+(vals['x2']-vals['x1'])**2)))
