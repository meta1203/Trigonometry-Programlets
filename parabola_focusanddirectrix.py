from stdutils import prettyFunction, inputAsDict

print("Focus: (a,b)")
print("Directrix: y = c")

values = inputAsDict(('a','b','c'))
formatValues = {'a': -values['a'], 'b': values['b']**2-values['c']**2, 'c': 2*(values['b']-values['c'])}

print("The equation of the parabola is:")
print(prettyFunction("y=((x{a&})^2{b&})/{c!}",formatValues))
