def MaximumPrizes(n):
    d = set()
    current = 1
    while True:
        #n became 0 current is the last element to add
        if n-current ==0:
            d.add(current)
            break
        #element already token
        if n-current <=current:
            current +=1
            continue
        #add element 
        d.add(current)
        n -= current
        current +=1
    return d
if __name__ =='__main__':
    n = int(input())
    result = MaximumPrizes(n)
    #print the number of elements
    print(len(result))
    #print all elements
    for elt in result:
        print(elt,end=" ")