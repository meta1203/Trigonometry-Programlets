import math
from fractions import Fraction

primes = [2,3,5,7,11]
symbols = {'degree': '°', 'root': '√', 'pi': 'π'}

class NiceValue:
    def __init__(self, base, root=1, pi=False):
        self.base = base
        self.root = root
        self.pi = pi
    def getFloat(self):
        return self.base*math.sqrt(self.root)*(math.pi if self.pi else 1)
    def getString(self):
        return '{:.6g}'.format(self.base) + ((symbols['root']+str(self.root)) if self.root else '') + ((symbols['pi']) if self.pi else '')

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

def isRational(val): # This totally works 100% of the time. Trust me.
    return Fraction(val).limit_denominator().denominator < 1000
