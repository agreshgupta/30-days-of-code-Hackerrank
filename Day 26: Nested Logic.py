#Enter your code here. Read input from STDIN. Print output to STDOUT
rd,rm,ry=input().split()
d,m,y = input().split()
#You can also use map function to do convert each element in integer
rd,rm,ry,d,m,y=int(rd),int(rm),int(ry),int(d),int(m),int(y)
if y<ry:
    print (10000)
elif ry == y:
    # Using if-else statement inside of if-else statement it is called Nested if-else.
    # you can nest the combination of loops and conditionals statements also but always remember more you use nested loops generally increase is time complexity.
    # Try to use this logic only for conditional statements aviod using it in loops try to find alternates.
    if m<rm:
        print (500*(rm-m))
    elif rm==m:
        if d<rd:
            print (15*(rd-d))
        else:
            print (0)
    else:
        print (0)
else:
    print(0)
