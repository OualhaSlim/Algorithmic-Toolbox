def GCD(a,b):
    if a ==0:
        return b
    return GCD(b%a,a)

def LCM(a,b):
    #LCM(a,b) = (a*b)//GCD(a,b)
    return (a*b)//GCD(a,b)

if __name__ =='__main__':
    a, b = map(int, input().split())
    print(LCM(a,b)) 