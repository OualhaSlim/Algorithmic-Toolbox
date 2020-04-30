def maximumAdRevenue(A,B):
    #sort the two arrays to obtain the maximum revenue
    A = sorted(A)
    B = sorted(B)
    result = 0
    for a,b in zip(A,B):
        result += a*b
    return result

if __name__ =='__main__':
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    print(maximumAdRevenue(A,B))