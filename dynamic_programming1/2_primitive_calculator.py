import math     

def calculator(n):    
    num_operations = [0, 0] + [math.inf]*(n-1)

    #find the minimum number of operations with filling num_operations in increasing order
    for i in range(2, n+1):
        temp1, temp2, temp3 = [math.inf]*3

        temp1 = num_operations[i-1] + 1 
        if i%2 == 0: temp2 = num_operations[i//2] + 1
        if i%3 == 0: temp3 = num_operations[i//3] + 1
        min_ops = min(temp1, temp2, temp3)
        num_operations[i] = min_ops

    print(num_operations[n])

    
    nums = [n]
    while n!=1:
        #make sure that deviding by 3 is better than substracting 1 otherwise it would be better to substract
        if n%3 ==0 and num_operations[n]-1 == num_operations[n//3]:
            nums += [n//3]
            n = n//3
        #make sure that deviding by 2 is better than substracting 1 otherwise it would be better to substract
        elif n%2 ==0 and num_operations[n]-1 == num_operations[n//2]:
            nums += [n//2]
            n = n//2
        else:
            nums += [n-1]
            n = n - 1

    return nums
        


if __name__ =='__main__':
    n = int(input())
    d = calculator(n)
    for elt in d[::-1]:
        print(elt,end=" ")