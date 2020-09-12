#!/bin/python3
#A easy problem and A easy solution
# but let me tell you it may pass all test cases but still it is not the correct way to solve the problem 
# Try to search about the topic 'RegEx, Patterns, and Intro to Databases in python' it is really a interesting topic.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    arr=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        a = emailID.split("@",1)
        if a[1] == "gmail.com" :
            arr.append(firstName)
    arr.sort()
    for i in range(len(arr)):
        print (arr[i])
