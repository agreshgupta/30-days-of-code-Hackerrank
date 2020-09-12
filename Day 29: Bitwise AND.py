#Bitwise AND unlocks a lot of possiblities in the programing world
#It helps to come up with better algorithms and it is really a interesting topic
import math
import os
import random
import re
import sys

def ToBinary(n):
    #Converting n from decimal to binary 
    return bin(n).replace("0b","") 

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        maxab = 0

        for a in range(n-1, 1, -1):

            for b in range(n, a, -1):
                #using AND operater 
                ab = a&b

                if ab < k and ab > maxab:
                    maxab = ab
                if maxab == k-1:
                    break

            if maxab == k-1:
                break
        print (maxab)

      
