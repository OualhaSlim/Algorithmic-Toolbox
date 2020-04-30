def find(s,f,l1,num):
    if s>f:
        print(-1,sep=" ")
        return None
    if l1[s]==num:
        print(s,sep=" ")
        return None
    elif l1[f]==num:
        print(f,sep=" ")
        return None
    m = (s+f)//2
    if l1[m]==num:
        print(m,sep=" ")
        return None
    elif num < l1[m]:
        find(s,m-1,l1,num)
    else:
        find(m+1,f,l1,num)



if __name__ =='__main__':
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    n = l1.pop(0)
    l2.pop(0)
    for num in l2:
        find(0,n-1,l1,num)