import math

# Определяем класс узла для связного списка
class Node:
    def __init__(self, data):
        # Данные, хранящиеся в узле (пара координат)
        self.data = data
        # Ссылка на следующий узел
        self.next = None

# Определяем класс кольцевой очереди на базе связного списка
class CircularQueue:
    def __init__(self):
        # Указатель на последний узел в очереди
        self.tail = None
        # Количество элементов в очереди
        self.size = 0

    def enqueue(self, data):
        # Создаем новый узел с данными
        new_node = Node(data)
        # Если очередь пуста
        if self.tail is None:
            # Новый узел указывает на себя, образуя кольцо
            new_node.next = new_node
            # Устанавливаем tail на новый узел
            self.tail = new_node
        else:
            # Вставляем новый узел после tail и обновляем tail
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        # Увеличиваем размер очереди
        self.size += 1

    def is_empty(self):
        # Проверяем, пуста ли очередь
        return self.tail is None

    def clear(self):
        # Очищаем очередь
        self.tail = None
        self.size = 0

    def __len__(self):
        # Возвращаем размер очереди
        return self.size

# Функция сортировки расчёской над кольцевой очередью
def comb_sort(queue):
    # Инициализируем количество элементарных операций
    operation_count = 0
    # Инициализируем размер шага
    gap = queue.size
    operation_count += 1  # Присваивание
    # Инициализируем коэффициент уменьшения шага
    shrink = 1.3
    operation_count += 1  # Присваивание
    # Флаг для отслеживания состояния сортировки
    sorted = False
    operation_count += 1  # Присваивание

    # Цикл продолжается, пока список не будет отсортирован
    while not sorted:
        operation_count += 1  # Проверка условия цикла
        # Обновляем размер шага
        gap = int(gap / shrink)
        operation_count += 1  # Операция деления и присваивания
        # Если шаг меньше 1, устанавливаем его равным 1
        if gap <= 1:
            gap = 1
            operation_count += 1  # Присваивание
            sorted = True
            operation_count += 1  # Присваивание
        # Инициализируем текущий узел
        current = queue.tail.next  # Начало очереди
        operation_count += 1  # Присваивание
        # Инициализируем индекс
        i = 0
        operation_count += 1  # Присваивание

        # Выполняем проход по очереди с текущим шагом
        while i + gap < queue.size:
            operation_count += 1  # Проверка условия цикла
            # Инициализируем узлы для сравнения
            node_i = current
            operation_count += 1  # Присваивание
            node_j = current
            operation_count += 1  # Присваивание
            # Перемещаемся на gap позиций от текущего узла
            for _ in range(gap):
                node_j = node_j.next
                operation_count += 1  # Операция перехода к следующему узлу
            # Сравниваем данные узлов по x-координате
            if node_i.data[0] > node_j.data[0]:
                operation_count += 1  # Операция сравнения
                # Обмениваем данные узлов
                node_i.data, node_j.data = node_j.data, node_i.data
                operation_count += 3  # Три операции присваивания
                # Так как произошел обмен, устанавливаем sorted в False
                sorted = False
                operation_count += 1  # Присваивание
            # Переходим к следующему узлу
            current = current.next
            operation_count += 1  # Присваивание
            # Увеличиваем индекс
            i += 1
            operation_count += 1  # Присваивание

        # Дополнительная проверка для случая, когда gap равен 1
        # и последний элемент может быть не на своем месте
        operation_count += 1  # Проверка условия
        if gap == 1:
            # Проходим оставшиеся элементы
            operation_count += 1  # Присваивание
            current = queue.tail.next
            operation_count += 1  # Присваивание
            for _ in range(queue.size - 1):
                operation_count += 1  # Цикл for
                next_node = current.next
                operation_count += 1  # Присваивание
                # Сравниваем текущий и следующий узлы
                if current.data[0] > next_node.data[0]:
                    operation_count += 1  # Операция сравнения
                    # Обмениваем данные узлов
                    current.data, next_node.data = next_node.data, current.data
                    operation_count += 3  # Три операции присваивания
                    # Устанавливаем sorted в False
                    sorted = False
                    operation_count += 1  # Присваивание
                # Переходим к следующему узлу
                current = next_node
                operation_count += 1  # Присваивание

    # Возвращаем количество элементарных операций
    return operation_count

# Функция линейной интерполяции
def interpolate(x0, y0, x1, y1, x):
    # Вычисляем наклон прямой
    m = (y1 - y0) / (x1 - x0) if x1 != x0 else 0.0
    # Вычисляем значение y в точке x
    y = y0 + m * (x - x0)
    return y

# Функция интегрирования методом Гаусса-Лежандра
def gauss_legendre_integration(x0, y0, x1, y1):
    # Число точек для квадратуры
    n = 2
    # Узлы и веса для 2-точечной квадратуры на [-1, 1]
    nodes = [-1.0 / math.sqrt(3), 1.0 / math.sqrt(3)]
    weights = [1.0, 1.0]
    # Половина длины интервала
    dx = (x1 - x0) / 2.0
    # Середина интервала
    xm = (x1 + x0) / 2.0
    # Инициализируем интеграл
    integral = 0.0
    # Проходим по узлам квадратуры
    for i in range(n):
        # Преобразуем узел к интервалу [x0, x1]
        xi = xm + dx * nodes[i]
        # Если x1 == x0, устанавливаем xi = x0, чтобы избежать деления на ноль
        if x1 == x0:
            xi = x0
        # Вычисляем yi с помощью интерполяции
        yi = interpolate(x0, y0, x1, y1, xi)
        # Добавляем вклад в интеграл
        integral += weights[i] * yi
    # Умножаем на dx для получения итогового интеграла
    integral *= dx
    return integral

# Инициализируем кольцевую очередь
coordinate_queue = CircularQueue()

# Счетчик элементарных операций
operation_count = 0

# Открываем файл для чтения
with open('/home/every/dev/AISD_4th_sem_labs/ЛР 3/test.txt', 'r') as file:
    # Проходим по каждой строке файла
    for line in file:
        # Разбиваем строку на x и y
        x_str, y_str = line.strip().split()
        # Преобразуем строки в числа
        x = float(x_str)
        y = float(y_str)
        # Добавляем пару (x, y) в очередь
        coordinate_queue.enqueue((x, y))
        operation_count += 1  # Операция добавления

# Выполняем сортировку расчёской и получаем количество операций
sort_operations = comb_sort(coordinate_queue)
operation_count += sort_operations

# Инициализируем общий интеграл
total_integral = 0.0
# Инициализируем счетчик операций для интегрирования
integration_operations = 0

# Проверяем, что в очереди достаточно элементов для интегрирования
if coordinate_queue.size < 2:
    print("Недостаточно точек для интегрирования.")
else:
    # Начинаем с головы очереди
    current = coordinate_queue.tail.next
    # Проходим по всем узлам
    for _ in range(coordinate_queue.size - 1):
        # Получаем текущие точки
        x0, y0 = current.data
        x1, y1 = current.next.data
        # Вычисляем интеграл на текущем интервале
        integral = gauss_legendre_integration(x0, y0, x1, y1)
        # Добавляем к общему интегралу
        total_integral += integral
        integration_operations += 1  # Считаем как одну операцию на интервал
        # Переходим к следующему узлу
        current = current.next

# Выводим общий интеграл
print("Интеграл равен:", total_integral)
# Выводим количество элементарных операций
print("Количество элементарных операций:", operation_count + integration_operations)
