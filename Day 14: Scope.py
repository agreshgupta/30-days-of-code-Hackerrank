#easy question now we try to understand code with less explanation
#If you find it difficult feel free to contanct me through my github profile
class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
    def computeDifference(self):
        self.maximumDifference = (max(self.__elements) - min(self.__elements))
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
