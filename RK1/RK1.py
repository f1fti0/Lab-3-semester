from operator import itemgetter

class BookStore:
    def __init__(self, ID, NAME):
        self.id = ID
        self.name = NAME


class Book:
    def __init__(self, ID, NAME, IDSTORE):
        self.id = ID
        self.name = NAME
        self.idStore = IDSTORE


class MBookStore:
    def __init__(self, IDBOOK, IDSTORE):
        self.idBook = IDBOOK
        self.idStore = IDSTORE


books = [
    Book(1, "Вечный кошмар", 1),
    Book(2, "Забудь меня", 1),
    Book(3, "Перекрёсток судеб", 1),
    Book(4, "Любовь не вечна", 2),
    Book(5, "Два желания", 3),
    Book(6, "Мир лжецов", 3),
    Book(7, "Северные ветра", 1),
    Book(8, "Последняя остановка", 3),
    Book(9, "Множество лесов", 2)
]

stores = [
    BookStore(1, "Читай-Город"),
    BookStore(2, "Лабиринт"),
    BookStore(3, "Букбридж"),
]

mbs = [
    MBookStore(1, 1),
    MBookStore(2, 1),
    MBookStore(3, 1),
    MBookStore(4, 2),
    MBookStore(5, 3),
    MBookStore(6, 3),
    MBookStore(7, 1),
    MBookStore(8, 3),
    MBookStore(9, 2),
]


def main():
    one_to_many = [(a.name, b.name)
                   for a in books
                   for b in stores
                   if a.idStore == b.id]

    many_to_many_temp = [(a.name, b.idBook, b.idStore)
                         for a in books
                         for b in mbs
                         if a.id == b.idBook]

    many_to_many = [(a, d.name)
                    for a, b, c in many_to_many_temp
                    for d in stores if d.id == c]

    res1 = [sorted(one_to_many, key=itemgetter(0))]
    print(f'Задание Б1\n{res1}')

    res2 = []
    for a in stores:
        n = 0
        for b in books:
            if b.idStore == a.id:
                n += 1
        res2.append((a.name, n))
    res2.sort(key=itemgetter(1), reverse=True)
    print(f'Задание Б2\n{res2}')

    res3 = [many_to_many[i] for i in range(len(many_to_many)) if many_to_many[i][0][-2:] == 'ов']
    print(f'Задание Б3\n{res3}')

if __name__ == '__main__':
    main()
