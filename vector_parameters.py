import stdutils, math
from stdutils import inputAsDict, cTheta, niceRoot, cApprox
vals = inputAsDict(('X','Y'))

angle = niceRoot(math.atan(vals['Y']/vals['X']))
mag = niceRoot(math.sqrt(vals['X']**2 + vals['Y']**2))

print('|v| = {} ≈ {:.6g}'.format(mag.getString(),mag.getFloat()))
print('θ = {} ≈ {:.6g}'.format(angle.getString(),angle.getFloat()))
