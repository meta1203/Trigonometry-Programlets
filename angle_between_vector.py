import stdutils, math
from stdutils import inputAsDict, cTheta, niceRoot, cApprox
vals = inputAsDict(('X1','Y1','X2','Y2'))

mag1 = math.sqrt(vals['X1']**2 + vals['Y1']**2)
mag2 = math.sqrt(vals['X2']**2 + vals['Y2']**2)
dot = (vals['X2']*vals['X1'])+(vals['Y2']*vals['Y1'])

out = niceRoot(math.acos(dot/(mag1*mag2)))
outD = niceRoot(math.acos(dot/(mag1*mag2))*(180/math.pi))

print('θ = {} ≈ {:.6g}'.format(out.getString(), out.getFloat()))
print('θ = {}° ≈ {:.6g}°'.format(outD.getString(), outD.getFloat()))