def number_coins(m,l):
    if m<3:
        return m
    elif m<5:
        return 1
    if m in l.keys():
        return l[m]
    l[m] = min(number_coins(m-4,l)+1,number_coins(m-3,l)+1,number_coins(m-1,l)+1)
    return l[m]




if __name__ =='__main__':
    m = int(input())
    print(number_coins(m,{}))
    