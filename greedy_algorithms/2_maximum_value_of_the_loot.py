import sys
def loot(n,W,l):
    result = 0.0
    for i in range(n):
        if W ==0:
            return result
        if l[i][1]<= W:
            result += l[i][0]
            W -= l[i][1]
        else:
            result += W*(l[i][0]/l[i][1])
            return result
    return result            

if __name__ =='__main__':
    n,W = map(int,input().split())
    l = []
    for _ in range(n):
        v,w = map(int,input().split())
        l.append((v,w))
    l = sorted(l,key=lambda x:x[0]/x[1],reverse=True)
    print("%.3f" %loot(n,W,l))
    