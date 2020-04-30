def majority(n,l):
    d = {}
    occ = 0
    for num in l:
        if num not in d.keys():
            d[num] = 1
        else:
            d[num] += 1
        if occ < d[num]:
            occ = d[num]
    return 1 if occ > n//2 else 0
     
    



if __name__ =='__main__':
    n = int(input())
    l = list(map(int, input().split())) 
    print(majority(n,l))