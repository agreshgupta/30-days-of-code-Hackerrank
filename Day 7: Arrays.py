# Import some module so that we dont have to go back to import it when we use it.
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    #taking input 
    arr = list(map(int, input().strip().split()))
    # code using single array diclaration
    # for i in range(n,0,-1)
    #     print(arr[i], end="")
    y =list()
    # I used for loop and extra space but you can change the limits of loop to work with single array
    for i in range(n):
        #or you can use print(arr[n-1-i], end="") directly in for loop
        y.append(arr[n-1-i])
        print (y[i], end="")
