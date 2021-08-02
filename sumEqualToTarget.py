"""
In a list, find pair equal to the target
"""

L = [3,6,12,14]
target = 15
d = {}
def findPair(L):
  for i in L:
    if i in d:
      print("the pair found as %s and %s" %(i, d[i]))
      break
    else:
      d[target-i] = i
  else:
    print("no valid pair found")

findPair(L)