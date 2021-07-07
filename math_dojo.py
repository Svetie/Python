class MathDojo:
    def __init__(self):
        self.result = 0
    # def add(self, *nums):
    #     for i in nums:
    #         self.result += i
    #     return self
    def add(self, num, *nums):
        self.result += num
        if(len(nums) >= 1):
            for i in nums:
                self.result += i
        return self
    def subtract(self, num, *nums):
        self.result -= num
        if(len(nums) >= 1):
            for i in nums:
                self.result -= i
        return self

# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5

# run each of the methods a few more times and check the result!
# md.result = 5 already
y = md.add(5).add(5,5).result
print(y)

m = MathDojo()
z = m.add(10,10).add(10,10,10).subtract(20).result
print('z ', z)
