import math

# Определяем класс Deque для реализации структуры данных дек
class Deque:
    def __init__(self):
        # Внутренний список для хранения элементов дека
        self.items = []
    
    def PushBack(self, item):
        # Добавляем элемент в конец дека
        self.items.append(item)
    
    def PushFront(self, item):
        # Добавляем элемент в начало дека
        self.items.insert(0, item)
    
    def PopBack(self):
        # Удаляем и возвращаем элемент из конца дека
        if self.IsEmpty():
            raise IndexError("PopBack from empty Deque")
        return self.items.pop()
    
    def PopFront(self):
        # Удаляем и возвращаем элемент из начала дека
        if self.IsEmpty():
            raise IndexError("PopFront from empty Deque")
        return self.items.pop(0)
    
    def IsEmpty(self):
        # Проверяем, пуст ли дек
        return len(self.items) == 0
    
    def Clear(self):
        # Очищаем дек
        self.items = []

# Инициализируем дек для хранения пар координат
coordinate_pairs = Deque()

# Открываем файл для чтения пар координат
with open('test.txt', 'r') as file:
    # Проходим по каждой строке в файле
    for line in file:
        # Разделяем строку на значения x и y
        try:
            x_str, y_str = line.strip().split()
        except:
            print("Входные данные идут не парами")
            exit()
        # Преобразуем строки в числа с плавающей запятой
        try:
            x = float(x_str)
            y = float(y_str)
        except:
            print("Входные данные не конвертируются в тип float")
            exit()
        # Добавляем пару координат в дек с помощью PushBack
        coordinate_pairs.PushBack((x, y))

def comb_sort(deque):
    # Инициализируем переменную для хранения длины дека
    size = 0
    # Копируем элементы дека в список для вычисления длины
    temp_deque = Deque()
    while not deque.IsEmpty():
        # Перемещаем элементы в временный дек и увеличиваем счетчик
        temp_deque.PushBack(deque.PopFront())
        size += 1
    # Возвращаем элементы обратно в исходный дек
    while not temp_deque.IsEmpty():
        deque.PushBack(temp_deque.PopFront())
    
    # Инициализируем переменные для сортировки
    gap = size  # Размер шага
    shrink = 1.3  # Коэффициент уменьшения шага
    sorted = False  # Флаг для отслеживания состояния сортировки

    # Цикл продолжается, пока список не будет отсортирован
    while not sorted:
        # Обновляем значение шага
        gap = int(gap / shrink)
        if gap <= 1:
            # Устанавливаем минимальный шаг равным 1
            gap = 1
            # Предполагаем, что это последний проход
            sorted = True
        # Инициализируем индексы для обхода дека
        index = 0
        while True:
            # Инициализируем временные деки для доступа к элементам по индексам
            front_deque = Deque()
            back_deque = Deque()
            # Перемещаем элементы из исходного дека в front_deque до индекса index
            for _ in range(index):
                if deque.IsEmpty():
                    break
                front_deque.PushBack(deque.PopFront())
            # Получаем первый элемент для сравнения
            if deque.IsEmpty():
                break
            first_item = deque.PopFront()
            # Перемещаем элементы в back_deque до элемента с индексом index + gap
            for _ in range(gap - 1):
                if deque.IsEmpty():
                    break
                back_deque.PushBack(deque.PopFront())
            # Проверяем, есть ли второй элемент для сравнения
            if deque.IsEmpty():
                # Возвращаем все элементы обратно
                front_deque.PushBack(first_item)
                while not back_deque.IsEmpty():
                    front_deque.PushBack(back_deque.PopFront())
                while not front_deque.IsEmpty():
                    deque.PushFront(front_deque.PopBack())
                break
            second_item = deque.PopFront()
            # Сравниваем элементы по x-координате
            if first_item[0] > second_item[0]:
                # Меняем элементы местами
                deque.PushFront(first_item)
                back_deque.PushBack(second_item)
                sorted = False
            else:
                deque.PushFront(second_item)
                back_deque.PushBack(first_item)
            # Возвращаем элементы обратно в исходный дек
            while not back_deque.IsEmpty():
                deque.PushFront(back_deque.PopBack())
            while not front_deque.IsEmpty():
                deque.PushFront(front_deque.PopBack())
            # Увеличиваем индекс
            index += 1
            if index + gap >= size:
                break

# Сортируем пары координат методом расчески
comb_sort(coordinate_pairs)

def interpolate(x0, y0, x1, y1, x):
    # Вычисляем наклон линии между двумя точками
    try:
        m = (y1 - y0) / (x1 - x0)
    except ZeroDivisionError:
        # print("Деление на ноль!")
        m = y1 - y0
    # Вычисляем интерполированное значение y в точке x
    y = y0 + m * (x - x0)
    return y

def gauss_legendre_integration(x0, y0, x1, y1):
    # Число точек для квадратуры Гаусса-Лежандра
    n = 2
    # Узлы для 2-точечной квадратуры Гаусса-Лежандра на интервале [-1, 1] (корни полинома Лежандра)
    nodes = [-1.0 / math.sqrt(3), 1.0 / math.sqrt(3)]
    # Веса для 2-точечной квадратуры Гаусса-Лежандра
    weights = [1.0, 1.0]
    # Половина длины интервала интегрирования
    dx = (x1 - x0) / 2.0
    # Середина интервала интегрирования
    xm = (x1 + x0) / 2.0
    # Инициализируем интеграл для текущего интервала
    integral = 0.0
    # Проходим по узлам квадратуры
    for i in range(n):
        # Преобразуем узел из интервала [-1, 1] в [x0, x1]
        xi = xm + dx * nodes[i]
        # Интерполируем значение y в точке xi
        yi = interpolate(x0, y0, x1, y1, xi)
        # Добавляем взвешенное значение функции к интегралу
        integral += weights[i] * yi
    # Умножаем на dx для получения значения интеграла на интервале
    integral *= dx
    return integral

# Инициализируем общий интеграл равным нулю
total_integral = 0.0

# Создаем временный дек для обхода coordinate_pairs
temp_deque = Deque()

# Проходим по парам координат для вычисления интеграла на каждом интервале
while not coordinate_pairs.IsEmpty():
    # Получаем начальную точку интервала
    x0, y0 = coordinate_pairs.PopFront()
    # Копируем начальную точку в temp_deque для последующего использования
    temp_deque.PushBack((x0, y0))
    # Проверяем, есть ли следующая точка
    if not coordinate_pairs.IsEmpty():
        # Получаем конечную точку интервала
        x1, y1 = coordinate_pairs.items[0]  # Используем прямой доступ к первому элементу
        # Вычисляем интеграл на текущем интервале методом Гаусса-Лежандра
        integral = gauss_legendre_integration(x0, y0, x1, y1)
        # Добавляем вычисленный интеграл к общему интегралу
        total_integral += integral

# Возвращаем элементы обратно в coordinate_pairs
while not temp_deque.IsEmpty():
    coordinate_pairs.PushFront(temp_deque.PopBack())

# Выводим общий вычисленный интеграл
print("Интеграл равен:", total_integral)
