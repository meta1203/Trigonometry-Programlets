# A module for various math-related functions

# Special Unicode characters
specials = {'pi': 'π', 'degree': '°', 'theta': 'θ', 'approx': '≈'}

# Formats equations using a dictionary of values
def prettyFunction(stringBase, values):
  # Insert special characters
  newString = stringBase.replace("{pi}",specials['pi'])
  newString = newString.replace("{degree}",specials['degree'])
  newString = newString.replace("{approx}",specials['approx'])
  newString = newString.replace("{theta}",specials['theta'])
  newString = newString.replace("&}",":+.6g}") # Have {foo&} insert the value foo with it's sign and rounded to 6 significant digits
  newString = newString.replace("!}",":-.6g}") # Have {foo&} insert the value foo rounded to 6 significant digits
  newString = newString.format(**values) # Add dictionary values
  return newString

# Obtain a list of arguments from the user
def inputAsDict(arguments):
  return {x: eval(input(x+": ")) for x in arguments}

# Rounds a value to 6 significant digits
def prettyFloat(value):
  return "{:.6g}".format(value)
