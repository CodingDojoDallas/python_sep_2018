class MathDojo:
    def __init__(self):
        self.value = 0

    def add(self, *nums):
        for i in nums:
            self.value += i
        return self

    def subtract(self, *nums):
        for i in nums:
            self.value -= i
        return self

    def result(self):
        print(self.value)