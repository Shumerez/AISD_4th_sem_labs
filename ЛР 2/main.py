class Deque:
    def __init__(self):
        self._higher_stack = list()
        self._lower_stack = list()

    # проверка на наличие элементов
    def empty(self):
        return len(self._higher_stack) == 0 and len(self._lower_stack) == 0 

    # (запись в конец) — операция вставки нового элемента в конец
    def push_low(self, x):
        self._lower_stack.append(x)

    # (снятие с конца) — операция удаления конечного элемента
    def pop_low(self):
        try:
            return self._lower_stack.pop
        except IndexError:
            if len(self._higher_stack) == 0:
                print("ОШИБКА ОБРАБОТАНА: pop from _lower empty stack")
                return
            else:
                # Переложить половину верхнего стека в нижний стек
                self._lower_stack += self._higher_stack[0:((len(self._higher_stack) + 1) // 2)]
                return self._lower_stack.pop

    # (запись в начало) — операция вставки нового элемента в начало
    def push_high(self, x):
        self._higher_stack.append(x)

    # (снятие с начала) — операция удаления начального элемента
    def pop_high(self):
        try:
            return self._higher_stack.pop
        except IndexError:
            if len(self._lower_stack) == 0:
                print("ОШИБКА ОБРАБОТАНА: pop from _lower empty stack")
                return
            else:
                # Переложить половину нижнего стека в верхний стек
                self._higher_stack += self._lower_stack[0:((len(self._lower_stack) + 1) // 2)]
                return self._higher_stack.pop

    # debug method, not a part of formal realisation
    def print_contents(self):
        self._higher_stack.reverse()
        for element in self._higher_stack:
            print(element)
        self._higher_stack.reverse()
        for element in self._lower_stack:
            print(element)


# Гачко, работа 2
# Разработать программу интегрирования методом Гаусса, считывая пары координат из файла и сортируя их расческой. Использовать дек.

# Как считать веса?

# I = sum[1->N](c_i*f(x_i))

# N - кол-во узлов, дано
# с_i - вес для узла i
# x_i - координата x для узла i
# f(x_i) - координата y для узла i


# Файлы с тестовыми данными:
# Тест 1
# String filenameForTest1 - относительный путь к файлу с входными данными для теста 1
filenameForTest1 = 'numbers_with_string.txt'
# Тест 2
# String filenameForTest2 - относительный путь к файлу с входными данными для теста 2
filenameForTest2 = 'numbers_float_overflow.txt'
# Тест 3 
# String filenameForTest3 - относительный путь к файлу с входными данными для теста 3
filenameForTest3 = 'numbers_valid.txt'
# Файл вывода
# String filenameOutput - относительный путь к файлу с выходными данными
filenameOutput = 'sorted_numbers_output.txt'

def input_and_validity_check(input_filename=filenameForTest3, output_filename=filenameOutput, testing_mode=False):
    # Float List numbers - Массив, в котором содержатся сортируемые числа в ходе работы программы
    numbers = Deque()
    # Ввод из файла
    with open(input_filename, 'r') as file:
        # String List content - относительный путь к файлу с входными данными
        coordinates = file.read().splitlines()
        for pair in coordinates:
            numbers.push_high(pair.split()[0]) # x - координата
            numbers.push_low(pair.split()[1]) # y - координата

    # numbers.print_contents()


    return
    # # Конвертация полученного массива строк в массив чисел типа float
    # for str_number in content:
    #     try:
    #         numbers.append(float(str_number))

    #     # Обработка случая, когда в файле предоставлены не float
    #     except ValueError:
    #         print("ОШИБКА: Файл содержит данные, не приводимые к типу float")
    #         return

    #     # Обработка случая, когда в файле предоставлены числа, большие float
    #     # raise OverflowError() - имеется в виду обработка этого исключения
    #     if (float(str_number) == float(str_number) + 1):
    #         print("ОШИБКА: Файл содержит числа, превышающие размер типа данных float")
    #         return




def __main__():
    input_and_validity_check(input_filename=r'C:\Users\Gregory\Documents\GitHub\AISD_4th_sem_labs\ЛР 2\test.txt')


    return 0

__main__()