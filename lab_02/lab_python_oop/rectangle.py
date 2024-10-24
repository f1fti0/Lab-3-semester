from lab_python_oop.figure import Figure
from lab_python_oop.color_figure import ColorFigure


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
