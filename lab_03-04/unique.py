class Unique(object):
    def __init__(self, items, **kwargs):
        if "ignore_case" in kwargs.keys():
            self.ignore_case = kwargs.get("ignore_case")
        else:
            self.ignore_case = False
        self.data = items
        self.arr = []
        self.number = -1

    def __next__(self):
        self.number += 1
        try:
            if isinstance(self.data[self.number], str):
                if self.ignore_case:
                    arg = self.data[self.number].lower()
                else:
                    arg = self.data[self.number]
                if arg not in self.arr:
                    self.arr.append(arg)
                    return arg
                else:
                    return self.__next__()
            elif self.data[self.number] not in self.arr:
                self.arr.append(self.data[self.number])
                return self.data[self.number]
            else:
                return self.__next__()
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


def test():
    from gen_random import gen_random
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data2 = gen_random(10, 1, 3)
    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print([i for i in Unique(data1)])
    print([i for i in Unique(data2)])
    print([i for i in Unique(data3)])
    print([i for i in Unique(data3, ignore_case=True)])

#test()
