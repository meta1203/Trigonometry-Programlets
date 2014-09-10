from stdutils import prettyFunction, inputAsDict

print("y = ax^2+bx+c\n")
values = inputAsDict(('a','b','c'))

computed = {'h': -values['b']/(2*values['a']), 'k': (4*values['a']*values['c']-values['b']**2)/(4*values['a'])}

print("Vertex of parabola:")
print(prettyFunction("({h!},{k!})", computed))
