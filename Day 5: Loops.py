#some basic libraries
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    #print out the desire output
    for i in range(10):
        #converting ints to str to print out the same datatype but you can also use format method or commas
        print (str(n) + " x " + str(i+1) + " = " + str(n*(i+1)))
