import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def square(self):
        pass


class ColorFigure:
    def __init__(self, COLOR):
        self.color = COLOR

    def __repr__(self):
        return f'{self.color}'


class Circle(Figure):
    def __init__(self, RADIUS, COLOR):
        self.name = "Circle"
        self.radius = RADIUS
        self.color = ColorFigure(COLOR)

    def __repr__(self):
        return f'Figure: {self.name}, Radius: {self.radius}, Color: {self.color}, Square: {self.square()}'

    def square(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Figure):
    def __init__(self, HEIGHT, WIDTH, COLOR):
        self.name = "Rectangle"
        self.height = HEIGHT
        self.width = WIDTH
        self.color = ColorFigure(COLOR)

    def __repr__(self):
        return f'Figure: {self.name}, Height: {self.height}, Width: {self.width}, Color: {self.color}, Square: {self.square()}'

    def square(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, HEIGHT, COLOR):
        super().__init__(HEIGHT, HEIGHT, COLOR)
        self.name = "Square"
        self.color = ColorFigure(COLOR)

    def __repr__(self):
        return f'Figure: {self.name}, Side of square: {self.height}, Color: {self.color}, Square: {self.square()}'
