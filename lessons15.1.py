import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def _calculate_dimensions(self, area):
        width = int(math.sqrt(area))
        while area % width != 0:
            width -= 1
        height = area // width
        return width, height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_square = self.get_square() + other.get_square()
            new_width, new_height = self._calculate_dimensions(new_square)
            return Rectangle(new_width, new_height)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)) and n > 0:
            new_square = self.get_square() * n
            new_width, new_height = self._calculate_dimensions(new_square)
            return Rectangle(new_width, new_height)
        return NotImplemented

    def __str__(self):
        return f"Rectangle({self.width}, {self.height}) with area {self.get_square()}"


r1 = Rectangle(2, 4)  # Площа 8
r2 = Rectangle(3, 6)  # Площа 18
assert r1.get_square() == 8
assert r2.get_square() == 18

r3 = r1 + r2
assert r3.get_square() == 26

r4 = r1 * 4
assert r4.get_square() == 32

assert Rectangle(3, 6) == Rectangle(2, 9)
print(r1)
print(r2)
print(r3)
print(r4)
