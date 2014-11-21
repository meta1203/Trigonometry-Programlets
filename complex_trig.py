import stdutils, math
from stdutils import inputAsDict, cTheta, niceRoot, cApprox
vals = inputAsDict(('size',cTheta))

real = math.cos(vals[cTheta])
comp = math.sin(vals[cTheta])

str1 = '{} ({} + i {})'.format(niceRoot(vals['size']).getString(),niceRoot(real).getString(),niceRoot(comp).getString())
str2 = '{} + {} i'.format(niceRoot(vals['size']*real).getString(),niceRoot(vals['size']*comp).getString())
str3 = '{} + {} i'.format(vals['size']*real, vals['size']*comp)

print('{} = {} {} {}'.format(str1, str2, cApprox, str3))