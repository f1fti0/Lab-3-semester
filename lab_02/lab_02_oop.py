import math
from abc import ABC


class Figure(ABC):
    def __init__(self, COLOR):
        self.color = COLOR

    def square(self):
        pass


class Circle(Figure):
    def __init__(self, RADIUS, COLOR):
        super().__init__(COLOR)
        self.name = "Circle"
        self.radius = RADIUS

    def __repr__(self):
        return f'Figure: {self.name}, Radius: {self.radius}, Color: {self.color}'

    def square(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Figure):
    def __init__(self, HEIGHT, WIDTH, COLOR):
        super().__init__(COLOR)
        self.name = "Rectangle"
        self.height = HEIGHT
        self.width = WIDTH

    def __repr__(self):
        return f'Figure: {self.name}, Height: {self.height}, Width: {self.width}, Color: {self.color}'

    def square(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, HEIGHT, COLOR):
        super().__init__(HEIGHT, HEIGHT, COLOR)
        self.name = "Square"

    def __repr__(self):
        return f'Figure: {self.name}, Side of square: {self.height}, Color: {self.color}'
