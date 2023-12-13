class Rectangle:
    def __init__(self, a, c):
        if a[1] > c[1]:
            if a[0] < c[0]:
                self.a = a
                self.c = c
            else:
                self.a = (c[0], a[1])
                self.c = (a[0], c[1])
        else:
            if a[0] > c[0]:
                self.c = a
                self.a = c
            else:
                self.a = (a[0], c[1])
                self.c = (c[0], a[1])

    def perimeter(self):
        return round((abs(self.a[0] - self.c[0]) + abs(self.a[1] - self.c[1])) * 2, 2)

    def area(self):
        return round(abs(self.a[0] - self.c[0]) * abs(self.a[1] - self.c[1]), 2)

    def get_pos(self):
        return self.a

    def get_size(self):
        return (round(abs(self.a[0] - self.c[0]), 2), round(abs(self.a[1] - self.c[1]), 2))

    def move(self, dx, dy):
        self.a = (round(self.a[0] + dx, 2), round(self.a[1] + dy, 2))
        self.c = (round(self.c[0] + dx, 2), round(self.c[1] + dy, 2))

    def resize(self, width, height):
        self.c = (self.a[0] + width, self.a[1] + height)

    def turn(self):
        center = self.__get_center()
        a = (self.a[0], self.a[1])
        c = (self.c[0], self.c[1])
        self.a = (center[0] - (a[1] - center[1]), center[1] + (center[0] - a[0]))
        # self.c = (center[0] + (a[1] - center[1]), center[1] - (center[0] - a[0]))
        self.c = (center[0] + (center[1] - c[1]), center[1] - (c[0] - center[0]))

    def __get_center(self):
        return (round((self.a[0] + self.c[0]) / 2, 2), round((self.a[1] + self.c[1]) / 2, 2))

    def scale(self, scale_factor):
        center = self.__get_center()
        self.a = (center[0] - (center[0] - self.a[0]) * scale_factor,
                  center[1] + (self.a[1] - center[1]) * scale_factor)
        self.c = (center[0] + (self.c[0] - center[0]) * scale_factor,
                  center[1] - (center[1] - self.c[1]) * scale_factor)


# rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
# print(rect.get_pos(), rect.get_size(), sep='\n')
# rect.turn()
# print(rect.get_pos(), rect.get_size(), sep='\n')

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')
