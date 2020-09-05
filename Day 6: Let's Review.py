#Not Imported any of the module or libraries. Used basic modules
# Taking Input
N = int(input())
using for loop to run for each Input separtely
for i in range(N):
    S=list(input())
    #creating empty list
    a=[]
    b=[]
    for j in range(len(S)):
        if j%2==0:
            a.append(S[j])
        if j%2!=0:
            b.append(S[j])
    #printing to the console
    print ("".join(a) + " " + "".join(b))
