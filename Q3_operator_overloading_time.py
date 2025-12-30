
class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def __add__(self, other):
        total_m = self.m + other.m
        total_h = self.h + other.h + total_m // 60
        total_m %= 60
        return Time(total_h, total_m)

    def display(self):
        print(self.h, "hrs", self.m, "mins")

t1 = Time(3, 50)
t2 = Time(2, 20)
t3 = t1 + t2
t3.display()
