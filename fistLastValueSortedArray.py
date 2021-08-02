"""
find the starting and ending position of
a given target value in a sorted array
"""
#L = [10,11,9,14,8,11,0,11,13]
L = [10,11,11,11,14,15]

def findOccurance(L,target):
  lenL = len(L)
  indexArray = []
  left = 0
  right = lenL-1
  while(left <= right):
    mid = (right+left)//2
    if L[mid] == target:
      if L[mid-1] == L[mid]:
        right = mid-1
      elif L[mid+1] == L[mid]:
        minIndex = mid
        left = mid+1
      else:
        print("only single occurance")
    else:
      if L[mid] < target:
        left = mid+1
      else:
        right = mid-1      
  left = 0
  right = Len-1
  while(left <= right):
    mid = (right+left)//2
    if L