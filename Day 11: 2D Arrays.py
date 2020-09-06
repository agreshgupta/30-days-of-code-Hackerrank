#Importing some modules
import math
import os
import random
import re
import sys


#Function main
if __name__ == '__main__':
    arr = []
    a = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            #appending the sum of all the possible combinations
            x = arr[i][j]+arr[i+1][j+1]+arr[i+2][j+2]+arr[i+2][j]+arr[i][j+2]+arr[i][j+1]+arr[i+2][j+1]
            a.append(x)
    #printing out the maximum possible value
    print (max(a))
