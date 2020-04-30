import numpy as np
import sys

def optimal_weight(W,n, w):
    value = np.zeros((n+1, W+1))
    for i in range(1,n+1):
        #current gold weight
        current_w = w[i]
        for j in range(W+1):
            #take previous value
            value[i][j] = value[i-1][j]
            if current_w <= j:
                #either keep the previous value or take the value with the current gold or only the current gold
                value[i][j] = max(value[i][j],value[i-1][j-current_w]+current_w,current_w)
            
    return value


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    #initial value with no gold and no weight
    w.insert(0,0)
    value = optimal_weight(W,n, w)
    print(int(value[n][W]))