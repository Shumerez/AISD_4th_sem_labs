from graphviz import Digraph

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)  # Добавляем элемент в конец очереди

    def pop(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)  # Удаляем и возвращаем первый элемент очереди

    def size(self):
        return len(self.items)

    # Метод для отладки
    def show(self):
        for item in self.items:
            print(item)

    # Метод сортировки расчёской
    def comb_sort(self, key_index=0):
        gap = len(self.items)
        shrink = 1.3
        sorted = False

        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True

            i = 0
            while i + gap < len(self.items):
                if self.items[i][key_index] > self.items[i + gap][key_index]:
                    self.items[i], self.items[i + gap] = self.items[i + gap], self.items[i]
                    sorted = False
                i += 1

# Определение узла красно-черного дерева
class RBTreeNode:
    def __init__(self, key, value, color='red', left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.color = color  # 'red' или 'black'
        self.left = left
        self.right = right
        self.parent = parent

# Красно-черное дерево
class RedBlackTree:
    def __init__(self):
        self.nil = RBTreeNode(key=None, value=None, color='black')  # Нил-узел (sentinel)
        self.root = self.nil

    def insert(self, key, value):
        # Создаем новый узел
        node = RBTreeNode(key, value)
        node.left = self.nil
        node.right = self.nil
        node.parent = None

        parent = None
        current = self.root

        # Поиск места для вставки
        while current != self.nil:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node  # Дерево было пустым
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = 'red'
        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    # Случай 1
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Случай 2
                        node = node.parent
                        self.left_rotate(node)
                    # Случай 3
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    # Случай 1
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Случай 2
                        node = node.parent
                        self.right_rotate(node)
                    # Случай 3
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
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
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    # Метод для визуализации дерева с помощью Graphviz
    def visualize(self, filename='rbtree'):
        dot = Digraph()
        dot.node(name='nil', label='NIL', shape='circle', color='black')

        def add_nodes_edges(node):
            if node != self.nil:
                node_name = str(id(node))
                # Создаем узел
                dot.node(name=node_name, label=str(node.key), shape='circle',
                         style='filled', fillcolor=('red' if node.color == 'red' else 'black'),
                         fontcolor='white' if node.color == 'black' else 'black')

                # Левый ребенок
                if node.left != self.nil:
                    left_name = str(id(node.left))
                    add_nodes_edges(node.left)
                else:
                    left_name = 'nil'
                dot.edge(node_name, left_name, label='L')

                # Правый ребенок
                if node.right != self.nil:
                    right_name = str(id(node.right))
                    add_nodes_edges(node.right)
                else:
                    right_name = 'nil'
                dot.edge(node_name, right_name, label='R')

        add_nodes_edges(self.root)
        dot.render(filename, view=True, format='png')

# Основная часть программы
# Инициализация очереди
my_coords = Queue()

# Считываем данные из файла и добавляем в очередь
with open('test.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue  # Пропускаем пустые строки
        numbers = line.split()
        if len(numbers) != 2:
            print(f"Строка '{line}' не содержит ровно два числа. Пропускаем.")
            continue
        try:
            x, y = map(int, numbers)
            my_coords.push([x, y])
        except ValueError:
            print(f"Не удалось преобразовать строку '{line}' в числа. Пропускаем.")

LEJANDRE_COORDINATES = {
    'n = 1': [0],
    'n = 2': [-0.5773503, 0.5773503],
    'n = 3': [-0.7745967, 0, 0.7745967],
    'n = 4': [-0.8611363, -0.3399810, 0.3399810, 0.8611363],
    'n = 5': [-0.9061798, -0.5384693, 0, 0.5384693, 0.9061798],
    'n = 6': [-0.9324700, -0.6612094, -0.2386142, 0.2386142, 0.6612094, 0.9324700]
}

LEJANDRE_WEIGHTS = {
    'n = 1': [2],
    'n = 2': [1, 1],
    'n = 3': [0.5555556, 0.8888889, 0.5555556],
    'n = 4': [0.3478548, 0.6521451, 0.6521451, 0.3478548],
    'n = 5': [0.4786287, 0.2369269, 0.5688888, 0.2369269, 0.4786287],
    'n = 6': [0.1713245, 0.3607616, 0.4679140, 0.4679140, 0.3607616, 0.1713245]
}

# Считаем интеграл между по всей функции
def gauss(coordinates: Queue, Lejandre_Number: str = 'n = 2') -> float:


    lower_x_limit : float = coordinates.items[0][0] # lower X
    higher_x_limit : float = coordinates.items[coordinates.size() - 1][0]  # higher X

    # print(lower_x_limit)
    # print(higher_x_limit)

    Integral : float = 0

    for lejandre_coordinate in range(len(LEJANDRE_COORDINATES[Lejandre_Number])):
        
        interpolated_x_coordinate = lower_x_limit + ((higher_x_limit - lower_x_limit) * (LEJANDRE_COORDINATES[Lejandre_Number][lejandre_coordinate] + 1)) / 2
        interpolated_y_coordinate = interp_polynomial(interpolated_x_coordinate)

        value : float = interpolated_y_coordinate * LEJANDRE_WEIGHTS[Lejandre_Number][lejandre_coordinate]
        
        Integral += value
    
    Integral *= (higher_x_limit - lower_x_limit)/2
    print(f"\nЗначение интеграла = {Integral}")
    return Integral

def lagrange_interpolation(coordinates : Queue):
    """
    Создаёт функцию интерполяционного полинома Лагранжа на основе заданных точек.

    Параметры:
    coordinates : Queue
        Список координат x,ys заданных точек.

    Возвращает:
    polynomial : function
        Функция, которая принимает значение x и возвращает значение интерполяционного полинома в этой точке.
    """
    
    # Число заданных точек
    n = coordinates.size()
    
    def polynomial(x):
        """
        Вычисляет значение интерполяционного полинома в точке x.

        Параметры:
        x : float
            Точка, в которой нужно вычислить полином.

        Возвращает:
        y : float
            Значение полинома в точке x.
        """
        total = 0  # Инициализация суммы полинома

        # Проходим по каждому базисному полиному L_i(x)
        for i in range(n):
            # Инициализация базисного полинома L_i(x)
            L_i = 1

            # Вычисляем произведение для L_i(x)
            for j in range(n):
                if i != j:
                    # Умножаем на каждое (x - x_j) / (x_i - x_j)
                    numerator = x - coordinates.items[j][0]
                    denominator = coordinates.items[i][0] - coordinates.items[j][0]
                    L_i *= numerator / denominator

            # Добавляем вклад i-го базисного полинома в общую сумму
            total += coordinates.items[i][1] * L_i

        return total

    return polynomial

# Сортируем очередь
my_coords.comb_sort(key_index=0)

# Создаем красно-черное дерево и добавляем элементы из очереди
rb_tree = RedBlackTree()
for coord in my_coords.items:
    rb_tree.insert(coord[0], coord[1])

# Визуализируем дерево
rb_tree.visualize('red_black_tree')

# Создаем функцию для вычисления значений y для интегрирования методом Гаусса
interp_polynomial = lagrange_interpolation(my_coords)

# Задаем количество узлов
gauss(my_coords, Lejandre_Number = 'n = 2')

