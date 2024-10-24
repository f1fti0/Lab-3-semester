import sys
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    a = Rectangle(17, 17, 'blue')
    b = Circle(17, 'green')
    c = Square(17, 'red')

    print(f'{a}\n{b}\n{c}')

if __name__ == '__main__':
    sys.exit(main())
