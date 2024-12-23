def print_result(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__}')
        res = func(*args, **kwargs)
        if isinstance(res, dict):
            for i, j in res.items():
                print(f'{i} = {j}')
        elif isinstance(res, list):
            for i in res:
                print(f'{i}')
        else:
            print(f'{res}')
        return res
    return wrapper


def test():
    @print_result
    def test_1():
        return 1

    @print_result
    def test_2():
        return 'iu5'

    @print_result
    def test_3():
        return {'a': 1, 'b': 2}

    @print_result
    def test_4():
        return [1, 2]

    if __name__ == '__main__':
        print('!!!!!!!!')
        test_1()
        test_2()
        test_3()
        test_4()

#test()
