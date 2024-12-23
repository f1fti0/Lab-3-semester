import RK2
from operator import itemgetter
import unittest


class MyTestCase(unittest.TestCase):
    def test_task1(self):
        result = RK2.task1(RK2.get_one_to_many(RK2.books, RK2.stores))
        reference = [('Вечный кошмар', 'Читай-Город'), ('Два желания', 'Букбридж'), ('Забудь меня', 'Читай-Город'),
                     ('Любовь не вечна', 'Лабиринт'), ('Мир лжецов', 'Букбридж'), ('Множество лесов', 'Лабиринт'),
                     ('Перекрёсток судеб', 'Читай-Город'), ('Последняя остановка', 'Букбридж'), ('Северные ветра', 'Читай-Город')]
        self.assertEqual(result, reference)

    def test_task2(self):
        result = RK2.task2(RK2.get_one_to_many(RK2.books, RK2.stores))
        reference = [('Читай-Город', 4), ('Букбридж', 3), ('Лабиринт', 2)]
        self.assertEqual(result, reference)

    def test_task3(self):
        result = RK2.task3(RK2.get_many_to_many(RK2.books, RK2.mbs))
        reference = [('Мир лжецов', 'Букбридж'), ('Множество лесов', 'Лабиринт')]
        self.assertEqual(result, reference)


if __name__ == '__main__':
    unittest.main()
