def fibonacci(n):
    if n <= 1:
        return n
    f0 = 0
    f1 = 1
    i = 2
    while(i<=n):
        f0,f2 = f1,f0+f1
        f1 = f2       
        i += 1
    return f2

if __name__ =='__main__':
    n = int(input())
    print(fibonacci(n))