from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color_figure import ColorFigure


class Square(Rectangle):
    def __init__(self, HEIGHT, COLOR):
        super().__init__(HEIGHT, HEIGHT, COLOR)
        self.name = "Square"
        self.color = ColorFigure(COLOR)

    def __repr__(self):
        return f'Figure: {self.name}, Side of square: {self.height}, Color: {self.color}, Square: {self.square()}'
