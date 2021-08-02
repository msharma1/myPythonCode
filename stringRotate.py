ss1 = "waterwottle"
ss2 = "erwottlewax"

#ss1 = "abc" # 1 - cab - bca
#ss2 = "bca"


for i in range(len(ss1)):
  sTemp = f"{ss1[-1]}{ss1[0:-1]}"
  ss1 = sTemp
  print("ss1 after %sth iteration: %s" %(i,ss1))
  if ss1 == ss2:
    print("Rotation found")
    break
else:
  print("Rotation not found")
    
"""  
d1 = {}
d2 = {}

for ind, ele in enumerate(s1):
  #print("ind: ", ind)
  #print("ele: ", ele)
  if ele in d1.keys():
    d1[ele].append(ind)
    #print("d1: ", d1)
  else:
    d1[ele] = [ind]
    #print("d1: ", d1)

for ind, ele in enumerate(s2):
  if ele in d2.keys():
    d2[ele].append(ind)
    #print("d2: ", d2)
  else:
    d2[ele] = [ind]
    #print("d2: ", d2)
    
print(d1)
print(d2)
"""