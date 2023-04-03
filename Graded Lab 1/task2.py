class math_Func:
    def __init__(self, num):
        self.num = num

    def factorial(self):
        fact = 1
        for i in range(1, self.num + 1):
            fact = fact * i
        return fact
    
obj = math_Func(5)

print(obj.factorial())