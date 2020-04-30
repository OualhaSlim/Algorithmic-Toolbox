def rest(n,m):
    if n<= 1:
        return n
    f0 = 0
    f1 = 1
    i = 1
    loop_found = False  #check if loop is found
    seq1 = [0,1]        #initial seq for f0 and f1 cause m>=2
    
    while(i<n and not loop_found):
        f0,f2 = f1,(f0+f1)  #fibonacci calculation
        f1 = f2
        i += 1
        seq1.append(f2%m)   #append only the rest

        #check if we have a loop
        if seq1[:len(seq1)//2] == seq1[len(seq1)//2:]:
            loop_found = True
    
    #return Fn%m
    return seq1[n%len(seq1)]

if __name__ =='__main__':
    n, m = map(int, input().split())
    print(rest(n,m))