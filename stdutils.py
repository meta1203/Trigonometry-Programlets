specials = {'pi': 'π', 'degree': '°', 'theta': 'θ', 'approx': '≈'}

def prettyFunction(stringBase, values):
  newString = stringBase.replace("{pi}",specials['pi'])
  newString = newString.replace("{degree}",specials['degree'])
  newString = newString.replace("{approx}",specials['approx'])
  newString = newString.replace("{theta}",specials['theta'])
  newString = newString.replace("&}",":+.6g}")
  newString = newString.replace("!}",":-.6g}")
  newString = newString.format(**values)
  return newString

def inputAsDict(arguments):
  return {x: eval(input(x+": ")) for x in arguments}

def prettyFloat(value):
  return "{:.6g}".format(value)
