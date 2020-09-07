import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
noofswaps = int(0)
for i in range(n):
    for j in range(n-1):
        if (a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
            
            noofswaps += 1
    #This is a usefull step to decrese the runtime
    if (noofswaps == 0):
        break
#Printing out the Result
print ("Array is sorted in "+str(noofswaps)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[n-1]))
