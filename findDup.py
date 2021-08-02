"""
Given an array, return True if a duplicate found.
Else return False.
"""
L = [1,2,3,11]
d = {}
def findDup(L):
  for i in L:
    if i in d:
      print("True")
    else:
      d[i] = [i]
  else:
    print("False")
      
findDup(L)