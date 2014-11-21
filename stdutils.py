# A module for various math-related functions
import sys
import math
from fractions import Fraction

# Special Unicode characters
specials = {'pi': 'π', 'degree': '°', 'theta': 'θ', 'approx': '≈', 'root': '√'}
cTheta = 'θ'
cPi = 'π'
cDegree = '°'
cRoot = '√'
cApprox = '≈'

# Constants for a user to convert values in input
D2R = math.pi/180
SQRT = math.sqrt
PI = math.pi

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
    elif 'add' in k and v > 0 and v % 1 == 0:
      sValues[k] = "+" + str(v)
    elif 'add' in k and v > 0:
      sValues[k] = '+ (' + str(v) + ')'
    elif (v % 1) == 0:
      sValues[k] = str(v)
    else:
      sValues[k] = "(" + str(v) + ")"
  newString = newString.format(**sValues) # Add dictionary values
  return newString

def prettyFunction(stringBase):
  # Insert special characters
  newString = stringBase.replace("{pi}",specials['pi'])
  newString = newString.replace("{degree}",specials['degree'])
  newString = newString.replace("{approx}",specials['approx'])
  newString = newString.replace("{theta}",specials['theta'])
  return newString

def prettyFraction(frac, forceOp=False, forceFloat=False):
    if forceFloat:
      return str(float(frac))
    elif forceOp and frac > 0 and frac % 1 == 0:
      return "+" + str(frac)
    elif forceOp and frac > 0:
      return '+ (' + str(frac) + ')'
    elif (frac % 1) == 0:
      return str(frac)
    else:
      return "(" + str(frac) + ")"

# Obtain a list of arguments from the user
def inputAsDict(arguments):
  return {x: getFraction(float(eval(input(x+": ")))) for x in arguments}

# Rounds a value to 6 significant digits
def prettyFloat(value):
  return "{:.6g}".format(value)

def inputFraction(prompt):
  return getFraction(input(prompt))

def getFraction(flt):
  return Fraction(flt).limit_denominator()

def giveMenu(functionDict):
  resDict = {}
  outStr = "Options:\n"
  x = 0
  for k,v in functionDict.items():
    x+=1
    resDict[x] = v
    outStr = outStr + "{}: {}".format(str(k),x)
  print(outStr)
  userInput = int(input("Selection: "))
  final = resDict[userInput]
  if final is None:
      print("Invalid selection.")
      sys.exit(1)
  return final


primes = [2,3,5,6,7,8,10,11]

class NiceValue:
    def __init__(self, base, root=1, pi=False):
        self.base = getFraction(base)
        self.root = root
        self.pi = pi
    def getFloat(self):
        return self.base*math.sqrt(self.root)*(math.pi if self.pi else 1)
    def getString(self):
        return str(self.base) + ((specials['root']+str(self.root)) if self.root != 1 else '') + ((specials['pi']) if self.pi else '')

def niceRoot(val):
    if isRational(val):
        return NiceValue(val)
    for x in primes:
      if isRational(val/(math.sqrt(x)*math.pi)):
        return NiceValue(val/(math.sqrt(x)*math.pi),root=x,pi=True)
      elif isRational(val/math.sqrt(x)):
        return NiceValue(val/math.sqrt(x),root=x)
      else:
        continue
    return NiceValue(val)

def isRational(val): # This totally works 100% of the time. Trust me.
    return Fraction(val).limit_denominator().denominator < 1000

