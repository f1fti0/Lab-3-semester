import sys


def printEquation(arr):
    if len(arr) == 0:
        print("Решений нет")
        return

    n = 1
    for i in arr:
        print(f'Решение №{n}: {i}')
        n += 1
    return


def solveEquation(a, b, c):
    arr = set()
    d = b**2 - 4*a*c
    if d < 0:
        printEquation(arr)
        return

    d = d**0.5
    t1 = (-b + d)/2*a
    t2 = (-b - d)/2*a

    if t1 >= 0:
        arr.add(t1**0.5)
        arr.add(-t1**0.5)
    if t2 >= 0:
        arr.add(t2**0.5)
        arr.add(-t2**0.5)

    printEquation(arr)
    return arr


def getDataLine():
    try:
        a, b, c = map(float, input().split())
        solveEquation(a, b, c)
    except ValueError:
        getDataLine()
    return


def getDataConsole():
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
            solveEquation(a, b, c)
        except ValueError:
            getDataLine()
    else:
        getDataLine()
    return


getDataConsole()
