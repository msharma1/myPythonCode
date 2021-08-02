"""
Given an array of integers of size n and 
find maximum sum of k consecutive elements
"""

#L = [4,9,1,2,3,7,8,9,1,12,13,14,0]
L = [80,-50,90,100]
sumL = []
sum = 0
flag = 0
for ind,ele in enumerate(L):
  if ind != 0:
    sumL.append(ele+L[ind-1])
print(sumL)
print(max(sumL))    