"""
In an array, there is only one element
that is present one time. Find that
"""
L = [2,1,1,4,4]
d = {1:[],'n':[]}
def findSingleElement(L):
  for i in L:
    print("i: ", i)
    if i not in d[1]:
      d[1].append(i)
      print("d after appneding %s is %s " % (i,d))
    else:
      #d[1] = []
      d[1].remove(i)
      print("d after appneding multi %s is %s " % (i,d))

  print(d[1])
 
findSingleElement(L) 