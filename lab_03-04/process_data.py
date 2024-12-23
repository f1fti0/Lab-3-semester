import json
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from field import field
from gen_random import gen_random

path = 'data.json'
with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(list(str(x) for x in Unique(field(arg, 'job-name'), ignore_case=True)))


@print_result
def f2(arg):
    return list(filter((lambda x: 'программист' in x), arg))


@print_result
def f3(arg):
    return list(map((lambda x: str(x) + ' с опытом Python'), arg))


@print_result
def f4(arg):
    return list(f'{i}, зарплата {j} руб.'
                for i, j in zip(arg, gen_random(len(arg), 100_000, 200_000)))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
