import math
import re
import operator

ops = {"+": operator.add ,"-":operator.sub ,"*":operator.mul ,"/":operator.truediv}

def MinMax(i,j,op,m,M):
    _min =math.inf
    _max = -_min
    for k in range(i,j):
        a = int(ops[op[k]](M[(i,k)],M[(k+1,j)]))
        b = int(ops[op[k]](M[(i,k)],m[(k+1,j)]))
        c = int(ops[op[k]](m[(i,k)],m[(k+1,j)]))
        d = int(ops[op[k]](m[(i,k)],M[(k+1,j)]))
        _min = min(_min,a,b,c,d)
        _max = max(_max,a,b,c,d)
    
    return (_min,_max)

def parentheses(eq):
    # Using re.split() 
    # Splitting operators in String 
    l = re.split(r'(\D)', eq) 
    op = []
    ind = 1
    while ind<len(l): 
        op.append(l.pop(ind))
        ind+=1
    #minimum values
    m = {}
    #maximum values
    M = {}
    n = len(l)
    #initiate the numbers in m and M
    for i in range(n):
        m[(i,i)]=int(l[i])
        M[(i,i)]=int(l[i])
    for s in range(1,n):
        for i in range(n-s):
            j = i+s
            m[(i,j)],M[(i,j)] = MinMax(i,j,op,m,M)
    
    return M[(0,n-1)]

if __name__ =='__main__':
    eq = input()
    
    print(parentheses(eq))