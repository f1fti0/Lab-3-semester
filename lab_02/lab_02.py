import sys
import lab_02_oop as figure


def main():
    a = figure.Rectangle(17, 17, 'blue')
    b = figure.Circle(17, 'green')
    c = figure.Square(17, 'red')

    print(f'{a}\n{b}\n{c}')

if __name__ == '__main__':
    sys.exit(main())
