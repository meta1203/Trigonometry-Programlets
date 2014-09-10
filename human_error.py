import random

inputValue = float(input('Accurate value: '))
marginPM = inputValue*0.05
outputValue = inputValue + (random.uniform(0,marginPM*2)-marginPM)

print('{:.4g} with a 5% margin of error is {:.4g}.'.format(inputValue, outputValue))
