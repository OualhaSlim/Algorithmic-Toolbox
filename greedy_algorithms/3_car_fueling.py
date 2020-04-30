def number_stops(m,n,stops):
    current = 0
    nb =0
    last = -1
    while(current<=n):
        last = current
        while(current<=n) and (stops[current+1]-stops[last]<=m):
            current += 1
        if current == last:
            return -1
        elif(current<=n):
            nb +=1
    return nb



if __name__ =='__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int,input().split()))
    stops.insert(0,0)
    stops.append(d)
    print(number_stops(m,n,stops))