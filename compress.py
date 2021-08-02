"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


s = "aabcccccaaa"


def comp(s):
  count = 1
  finalString = ""
  for indexOuter,elementOuter in enumerate(s):
    if indexOuter == 0:
      count = 1
    else:
      if s[indexOuter-1] == elementOuter:
        if indexOuter != len(s)-1:
          count +=1
        else:
          finalString = f"{finalString}{s[indexOuter-1]}{str(count+1)}"
      else:
        finalString = f"{finalString}{s[indexOuter-1]}{str(count)}"
        count = 1
  print(finalString)
  
comp(s)
      

  
"""
def comp(s):
  finalString = ""
  listTemp = []
  count = 1
  for index,element in enumerate(s,count):
    innerTemp = []
    if element == s[index+1]:
      innerTemp.append(element)
    else:
      listTemp.extend(innerTemp.append(element))

  print(finalString)

comp(s)
"""
"""
d = {}
for i in s:
  if i in d.keys():
    d[i] += 1
  else:
    d[i] = 1

sFinal = ""    
print(d)
for k,v in d.items():
  sFinal.join(k+str(v))
print(sFinal)
"""