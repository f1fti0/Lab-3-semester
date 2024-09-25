import sys


class Equation:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.arr = set()

    def printEquation(self):
        if len(self.arr) == 0:
            print("Решений нет")
            return

        n = 1
        for i in self.arr:
            print(f'Решение №{n}: {i}')
            n += 1
        return

    def solveEquation(self):
        d = self.b ** 2 - 4 * self.a * self.c
        if d < 0:
            return

        d = d ** 0.5
        t1 = (-1 * self.b + d) / 2 * self.a
        t2 = (-1 * self.b - d) / 2 * self.a

        if t1 >= 0:
            self.arr.add(t1 ** 0.5)
            self.arr.add(-t1 ** 0.5)
        if t2 >= 0:
            self.arr.add(t2 ** 0.5)
            self.arr.add(-t2 ** 0.5)
        return

    def getValue(self):
        try:
            A, B, C = map(float, input().split())
            self.a = A
            self.b = B
            self.c = C
            self.solveEquation()
        except ValueError:
            self.getValue()
        return

    def getValueConsole(self):
        if len(sys.argv) == 4:
            try:
                self.a = float(sys.argv[1])
                self.b = float(sys.argv[2])
                self.c = float(sys.argv[3])
                self.solveEquation()
            except ValueError:
                self.getValue()
        else:
            self.getValue()
        return

a = Equation()
a.getValueConsole()
a.printEquation()
