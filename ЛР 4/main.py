import math

# Определяем класс очереди на базе массива
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Добавляем элемент в конец очереди
        self.items.append(item)

    def is_empty(self):
        # Проверяем, пуста ли очередь
        return len(self.items) == 0

    def clear(self):
        # Очищаем очередь
        self.items = []

    def __len__(self):
        # Возвращаем размер очереди
        return len(self.items)

# Функция сортировки расчёской
def comb_sort(array):
    gap = len(array)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(array):
            if array[i][0] > array[i + gap][0]:
                array[i], array[i + gap] = array[i + gap], array[i]
                sorted = False
            i += 1

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

def old_gauss_legendre_integration(x0, y0, x1, y1):
    # Number of points for quadrature
    n = 4
    # Nodes and weights for 4-point Gauss-Legendre quadrature on [-1, 1]
    nodes = [-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116]
    weights = [0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451]
    # Half the length of the interval
    dx = (x1 - x0) / 2.0
    # Middle of the interval
    xm = (x1 + x0) / 2.0
    # Initialize integral
    integral = 0.0
    # Perform quadrature
    for i in range(n):
        # Transform node to [x0, x1]
        xi = xm + dx * nodes[i]
        # Avoid division by zero
        if x1 == x0:
            xi = x0
        # Compute yi using interpolation
        yi = interpolate(x0, y0, x1, y1, xi)
        # Add to integral
        integral += weights[i] * yi
    # Scale by dx
    integral *= dx
    return integral

# Класс узла для красно-черного дерева
class RBNode:
    def __init__(self, key, value=None, color='RED', left=None, right=None, parent=None):
        self.key = key
        self.value = value  # Сохраняем значение y или пару (x, y)
        self.color = color  # 'RED' или 'BLACK'
        self.left = left if left else None
        self.right = right if right else None
        self.parent = parent

# Класс красно-черного дерева
class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, color='BLACK')
        self.root = self.NIL

    def insert(self, key, value=None):
        # Создаем новый узел
        node = RBNode(key, value)
        node.left = self.NIL
        node.right = self.NIL

        # Обычная вставка в бинарное дерево поиска
        y = None
        x = self.root

        while x != self.NIL and x.key is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y

        if y is None or y == self.NIL:
            self.root = node  # Дерево было пустым
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # Выполняем фиксацию для поддержания свойств красно-черного дерева
        self.insert_fixup(node)

    def insert_fixup(self, z):
        while z.parent != None and z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'RED':
                    # Случай 1
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        # Случай 2
                        z = z.parent
                        self.left_rotate(z)
                    # Случай 3
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'RED':
                    # Случай 1
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        # Случай 2
                        z = z.parent
                        self.right_rotate(z)
                    # Случай 3
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'BLACK'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None or x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None or y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    # Метод для обхода дерева в порядке (in-order)
    def inorder_helper(self, node):
        if node != self.NIL and node.key is not None:
            self.inorder_helper(node.left)
            print(f'Ключ: {node.key}, Значение: {node.value}, Цвет: {node.color}')
            self.inorder_helper(node.right)

    def print_tree(self):
        self.inorder_helper(self.root)

    # Функция для визуализации дерева
    def visualize_tree(self):
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Возвращает список строк, высоту и ширину поддерева."""
        if node == self.NIL or node.key is None:
            return ["Н", 1, 1, 0]  # Нил узел

        line_color = 'R' if node.color == 'RED' else 'B'
        line = f'{node.key}({line_color})'

        # Если нет дочерних узлов
        if node.left == self.NIL and node.right == self.NIL:
            width = len(line)
            height = 1
            middle = width // 2
            return [line], height, width, middle

        # Если только правый дочерний узел
        if node.left == self.NIL:
            lines, n, p, x = self._display_aux(node.right)
            s = line
            u = len(s)
            first_line = s + ' ' * (p)
            second_line = ' ' * (u) + '\\' + ' ' * (p - 1)
            shifted_lines = [ ' ' * u + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + 2, u + p, u // 2

        # Если только левый дочерний узел
        if node.right == self.NIL:
            lines, n, p, x = self._display_aux(node.left)
            s = line
            u = len(s)
            first_line = ' ' * (p) + s
            second_line = ' ' * (p - 1) + '/' + ' ' * (u)
            shifted_lines = [line + ' ' * u for line in lines]
            return [first_line, second_line] + shifted_lines, n + 2, p + u, p // 2

        # Если есть оба дочерних узла
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = line
        u = len(s)
        first_line = ' ' * (x + 1) + ' ' * (p - x - 1) + s + ' ' * y + ' ' * (q - y)
        second_line = ' ' * x + '/' + ' ' * (p - x -1 + u + y) + '\\' + ' ' * (q - y -1)
        if n < m:
            left += [' ' * p] * (m - n)
        elif m < n:
            right += [' ' * q] * (n - m)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + ' ' * u + b for a, b in zipped_lines]
        return lines, max(n, m) + 2, p + q + u, p + u // 2

# Инициализируем очередь
coordinate_queue = Queue()

# Параметры для проверки уникальности X
uniq_X = []

# Открываем файл для чтения
try:
    with open('./test.txt', 'r') as file:
        # Проходим по каждой строке файла
        for line in file:
            # Разбиваем строку на x и y
            try:
                x_str, y_str = line.strip().split()
                # Преобразуем строки в числа
                x = float(x_str)
                y = float(y_str)
                # Проверяем на уникальность X
                if x in uniq_X:
                    print("В вашем массиве координат есть некорректные значения")
                    exit()
                uniq_X.append(x)
                # Добавляем пару (x, y) в очередь
                coordinate_queue.enqueue((x, y))
            except:
                print("Входные данные не соответствуют формату")
                exit()
except FileNotFoundError:
    print("Файл 'test.txt' не найден.")
    exit()

# Выполняем сортировку расчёской
comb_sort(coordinate_queue.items)

# Инициализируем красно-черное дерево
rb_tree = RedBlackTree()

# Записываем результат сортировки в красно-черное дерево
for item in coordinate_queue.items:
    x, y = item
    rb_tree.insert(x, y)

# Инициализируем общий интеграл
total_integral = 0.0

# Проверяем, что в очереди достаточно элементов для интегрирования
if len(coordinate_queue) < 2:
    print("Недостаточно точек для интегрирования.")
else:
    # Проходим по всем узлам
    for i in range(len(coordinate_queue.items) - 1):
        # Получаем текущие точки
        x0, y0 = coordinate_queue.items[i]
        x1, y1 = coordinate_queue.items[i + 1]
        # Вычисляем интеграл на текущем интервале
        integral = gauss_legendre_integration(x0, y0, x1, y1)
        # Добавляем к общему интегралу
        total_integral += integral

# Выводим общий интеграл
print("Интеграл равен:", total_integral)

# Выводим содержимое красно-черного дерева
print("\nКрасно-черное дерево содержит следующие координаты (ключи):")
rb_tree.print_tree()

# Визуализируем дерево
print("\nВизуализация красно-черного дерева:")
rb_tree.visualize_tree()
