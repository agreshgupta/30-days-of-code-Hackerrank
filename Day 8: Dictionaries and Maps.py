# You can pre import some module for hazzle free coding
n = int(input().strip())
# Creating A dictionary 
phonebook=dict()
for _ in range(0,n):
    name,number = input().strip().split()
    phonebook[name]= number
# using While loops just a tip try using more of while loops instead of for it will help you to understand while loop
while(True):
#ignore try catch except for now but it is good habit to use it for writing more understable code.
    try:
        name = input().strip()
        if name in phonebook:
            print("{}={}".format(name, phonebook[name]))
        else:
            print("Not found")
    except EOFError:
        break
