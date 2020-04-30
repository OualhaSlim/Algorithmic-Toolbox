def CollectingSignatures(data):
    data = sorted(data,key=lambda x : x[1])
    visiteTime = []
    while data:
        aux = data.pop(0)[1]
        #remove period within the collection time
        while data:
            start = data[0][0]
            if start>aux:
                break
            data.pop(0)
        visiteTime.append(aux)
    return visiteTime

if __name__ =='__main__':
    n = int(input())
    data = []
    while n:
        A = list(map(int,input().split()))
        data.append(A)
        n -= 1 
    result = CollectingSignatures(data)
    print(len(result))
    for m in result:
        print(m,end=" ")