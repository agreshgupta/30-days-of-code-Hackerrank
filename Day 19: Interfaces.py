#Welcome to another amazing thing about OOP
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        pass
        arr =[]
        for i in range(1,n):
            if n%i==0:
                arr.append(i)
        return (sum(arr)+n)

# Decalaring a calculaor object
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
