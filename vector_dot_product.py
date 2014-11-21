import stdutils, math
from stdutils import inputAsDict, cTheta, niceRoot, cApprox
vals = inputAsDict(('X1','Y1','X2','Y2'))

dot = (vals['X2']*vals['X1'])+(vals['Y2']*vals['Y1'])

print('{} ≈ {:.6g}'.format(niceRoot(dot).getString(),niceRoot(dot).getFloat()))