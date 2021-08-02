def myFunc(L,LC):
    if len(L) > 0:
        for ind in range(0,len(L)):
            LC.append((L[ind]))
            #print("LC so far: ", LC)
            for j in L[ind:]:
                LC.append((L[ind] + j,j + L[ind]))
        myFunc(L[ind:],LC)
    return LC

if __name__ == '__main__':
    LF = myFunc("abc",[])
    print(LF)		
    
