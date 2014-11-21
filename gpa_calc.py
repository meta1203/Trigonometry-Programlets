point_vals = {'a': 4.0, 'a-': 3.7, 'b+': 3.33, 'b': 3.0, 'b-': 2.7, 'c+': 2.3, 'c': 2.0, 'c-': 1.7, 'd+': 1.3, 'd': 1.0, 'd-': 0.7, 'f': 0.0}

# Tuple for input
# (creditHours, grade)

def gradePoints(tuplInput):
  gradeStr = tuplInput[1].lower()
  return point_vals[gradeStr]*tuplInput[0]

def main():
  listOTuples = []
  hours = 0
  while True:
    val = input("Input # of credit hours (or 'stop' to stop): ")
    if "stop" in val.lower():
      break
    grade = input("Grade (eg. a, c+, b-): ")
    listOTuples.append((float(val),grade))
    hours = hours + float(val)
  total = 0
  for x in listOTuples:
    print("Credit hours: {:.6g}\t\tGrade: {}\t GP:{:.6g}".format(x[0],x[1].upper(),gradePoints(x)))
    total = total + gradePoints(x)
  print("Your GPA is: {:.6g}".format(total/hours))
  
def lowestToMeet():
  listOHours = []
  minGPA = float(input("Minimum GPA: "))
  
  while True:
    val = input("Input # of credit hours (or 'stop' to stop): ")
    if "stop" in val.lower():
      break
    listOHours.append(float(val))
  total = 0
  hours = 0
  for x in listOTuples:
    print("Credit hours: {:.6g}\t\tGrade: {}\t GP:{:.6g}".format(x[0],x[1].upper(),gradePoints(x)))
    total = total + gradePoints(x)
    hours = hours + x[0]
  print("Your GPA is: {:.6g}".format(total/hours))
  
if __name__ == '__main__':
  main()
