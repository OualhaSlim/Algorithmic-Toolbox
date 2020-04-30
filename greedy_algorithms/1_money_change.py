def number_coins(n):
    if n<5:
        return n
    elif n<10:
        return 1+n-5
    else:
        return (n//10)+number_coins(n%10)    


if __name__ =='__main__':
    n = int(input())
    print(number_coins(n))