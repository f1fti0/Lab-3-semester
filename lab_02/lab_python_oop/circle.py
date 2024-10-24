from lab_python_oop.figure import Figure
from lab_python_oop.color_figure import ColorFigure
from math import pi


class Circle(Figure):
    def __init__(self, RADIUS, COLOR):
        self.name = "Circle"
        self.radius = RADIUS
        self.color = ColorFigure(COLOR)

    def __repr__(self):
        return f'Figure: {self.name}, Radius: {self.radius}, Color: {self.color}, Square: {self.square()}'

    def square(self):
        return pi * (self.radius ** 2)
