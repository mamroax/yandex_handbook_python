class Rectangle:
    def __init__(self, a, c):
        self.a = a
        self.c = c

    def perimeter(self):
        return round((abs(self.a[0] - self.c[0]) + abs(self.a[1] - self.c[1])) * 2, 2)

    def area(self):
        return round(abs(self.a[0] - self.c[0]) * abs(self.a[1] - self.c[1]), 2)

rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())