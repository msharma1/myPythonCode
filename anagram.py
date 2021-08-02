"""
Program for anagram
input: ["eat", "tea", "tan", "ate", "nat", "bat"]
output: [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
"""
d = {}
L = ["eat", "tea", "tan", "ate", "nat", "bat"]
def anagram(L):
  for index,element in enumerate(L):
    HM = [0]*140
    print(element)
    a,b,c = tuple(element)
    print("abc are %s,%s,%s" % (ord(a),b,c))
    print(HM)
    print(HM[ord(a)])
    HM[ord(a)] = 1
    HM[ord(b)] = 1
    HM[ord(c)] = 1
    print("HM for element %s is: %s" %(element, HM))
    if tuple(HM) in d:
      d[tuple(HM)].append(element)
    else:
      d[tuple(HM)] = [element]
  LF = []    
  print(d)
  for k,v in d.items():
    LF.append(v)
  
  print(LF)
  
anagram(L)