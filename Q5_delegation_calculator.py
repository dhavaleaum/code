
class Calculator:
    def add(self, a, b):
        return a + b

class MathApp:
    def __init__(self):
        self.calc = Calculator()

    def addition(self, a, b):
        return self.calc.add(a, b)

m = MathApp()
print("Addition:", m.addition(10, 20))
