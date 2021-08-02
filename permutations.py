s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"

lenS = len(s)
premutations = []
for ind, ele in enumerate(b):
  lTemp = b[ind:ind+lenS]
  sTemp = s
  flag = 1
  for i in lTemp:
    if i in sTemp:
      print(i)
      sTemp.replace(i,'',1)
      print("sTemp", sTemp)
    else:
      break
  else:
    premutations.append(lTemp)
   
print(premutations)