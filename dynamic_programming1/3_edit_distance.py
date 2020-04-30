def edit(A,B,n,m,d):
    if m==0:
        return n
    if n==0:
        return m
    if (n,m) in d.keys():
        return d[(n,m)]
    #found same caracter
    if A[n-1]==B[m-1]:
        d[(n,m)] = edit(A,B,n-1,m-1,d)
        return d[(n,m)]
    else:
        #delete or modify or insert
        d[(n,m)] = 1+min(edit(A,B,n-1,m-1,d),min(edit(A,B,n-1,m,d),edit(A,B,n,m-1,d)))
        return d[(n,m)]




if __name__ =='__main__':
    A = list(input())
    B = list(input())
    #A = list('short')
    #B = list('ports')
    n = len(A)
    m = len(B)

    print(edit(A,B,n,m,{}))
    

