# A module for various math-related functions
from fractions import Fraction

# Special Unicode characters
specials = {'pi': 'π', 'degree': '°', 'theta': 'θ', 'approx': '≈'}
line = '─'

# Formats equations using a dictionary of values
def prettyFunction(stringBase, values):
  # Insert special characters
  newString = stringBase.replace("{pi}",specials['pi'])
  newString = newString.replace("{degree}",specials['degree'])
  newString = newString.replace("{approx}",specials['approx'])
  newString = newString.replace("{theta}",specials['theta'])
  sValues = {}
  for k,v in values.items():
    if 'float' in k:
      sValues[k] = str(float(v))
    elif 'add' in k and v > 0 and float(v % 1) is 0:
      sValues[k] = "+" + str(v)
    elif 'add' in k and v > 0:
      sValues[k] = '+ (' + str(v) + ')'
    elif float(v % 1) is 0:
      sValues[k] = str(v)
    else:
      sValues[k] = "(" + str(v) + ")"
  newString = newString.format(**sValues) # Add dictionary values
  return newString

# Obtain a list of arguments from the user
def inputAsDict(arguments):
  return {x: getFraction(float(eval(input(x+": ")))) for x in arguments}

# Rounds a value to 6 significant digits
def prettyFloat(value):
  return "{:.6g}".format(value)

def getFraction(flt):
  return Fraction(flt).limit_denominator()

