#This problem will change your idea about coding.
#New Coders are reqiured to come up with better and fast algorithms.
#importing sq. root function
from math import sqrt

T = int(input())

#using sq. root instead of number itself reduces it time complexity and results the same output
#Think what we again reduce this sq. root to its square will it result in faster algorithm?
def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i is 0:
            return False
    return True


for _ in range(T):
    n = int(input())

    if n >= 2 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")
