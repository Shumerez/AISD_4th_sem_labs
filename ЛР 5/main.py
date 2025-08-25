import math

# Определяем класс узла для связного списка (стека)
class Node:
    def __init__(self, data):
        # Данные, хранящиеся в узле (пара координат)
        self.data = data
        # Ссылка на следующий узел
        self.next = None

# Определяем класс стека на базе связного списка
class Stack:
    def __init__(self):
        # Указатель на вершину стека
        self.top = None
        # Размер стека
        self.size = 0

    def push(self, data):
        """Добавляет элемент на вершину стека"""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека"""
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        """Возвращает элемент с вершины стека без удаления"""
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        """Проверяет, пуст ли стек"""
        return self.top is None

    def __len__(self):
        """Возвращает размер стека"""
        return self.size

    def to_list(self):
        """Преобразует стек в список для сортировки"""
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, data_list):
        """Заполняет стек из списка"""
        self.clear()
        # Добавляем элементы в обратном порядке, чтобы первый элемент списка был на вершине
        for item in reversed(data_list):
            self.push(item)

    def clear(self):
        """Очищает стек"""
        self.top = None
        self.size = 0

# Функция быстрой сортировки (Quick Sort)
def quick_sort(arr, low=0, high=None):
    """Быстрая сортировка массива по x-координате"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Разделяем массив и получаем индекс опорного элемента
        pi = partition(arr, low, high)
        
        # Рекурсивно сортируем элементы до и после опорного
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    """Функция разделения для быстрой сортировки"""
    # Выбираем последний элемент как опорный
    pivot = arr[high][0]  # x-координата опорного элемента
    
    # Индекс меньшего элемента
    i = low - 1
    
    for j in range(low, high):
        # Если текущий элемент меньше или равен опорному
        if arr[j][0] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Размещаем опорный элемент в правильной позиции
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Функция линейной интерполяции
def interpolate(x0, y0, x1, y1, x):
    """Линейная интерполяция между двумя точками"""
    if x1 == x0:
        return y0
    # Вычисляем наклон прямой
    m = (y1 - y0) / (x1 - x0)
    # Вычисляем значение y в точке x
    y = y0 + m * (x - x0)
    return y

# Функция интегрирования методом Симпсона
def simpson_integration(x0, y0, x1, y1):
    """Интегрирование методом Симпсона на интервале [x0, x1]"""
    if x0 == x1:
        return 0.0
    
    # Средняя точка интервала
    x_mid = (x0 + x1) / 2.0
    
    # Интерполируем значение y в средней точке
    y_mid = interpolate(x0, y0, x1, y1, x_mid)
    
    # Формула Симпсона: (b-a)/6 * [f(a) + 4*f((a+b)/2) + f(b)]
    h = x1 - x0
    integral = (h / 6.0) * (y0 + 4 * y_mid + y1)
    
    return integral

# Класс для работы с бинарным деревом поиска
class BSTNode:
    def __init__(self, key, value):
        self.key = key      # x-координата
        self.value = value  # y-координата
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        """Вставка узла в бинарное дерево поиска"""
        if self.root is None:
            self.root = BSTNode(key, value)
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        """Рекурсивная вставка"""
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, value)
            else:
                self._insert_recursive(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, value)
            else:
                self._insert_recursive(node.right, key, value)
        # Если ключи равны, обновляем значение
        else:
            node.value = value

    def inorder_traversal(self):
        """Обход дерева в порядке возрастания ключей"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Рекурсивный обход"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append((node.key, node.value))
            self._inorder_recursive(node.right, result)

    def print_tree(self):
        """Печать дерева"""
        if self.root is None:
            print("Дерево пустое")
            return
        
        print("Бинарное дерево поиска (обход в порядке возрастания):")
        for key, value in self.inorder_traversal():
            print(f"Ключ: {key}, Значение: {value}")

# Инициализируем стек для координат
coordinate_stack = Stack()

# Параметры для проверки уникальности X
uniq_X = []

# Открываем файл для чтения
try:
    with open('test.txt', 'r') as file:
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
                    print("В вашем массиве координат есть некорректные значения (дублирующиеся x)")
                    exit()
                uniq_X.append(x)
                
                # Добавляем пару (x, y) в стек
                coordinate_stack.push((x, y))
                
            except ValueError:
                print("Входные данные не соответствуют формату")
                exit()
            except Exception as e:
                print(f"Ошибка обработки данных: {e}")
                exit()
                
except FileNotFoundError:
    print("Файл 'test.txt' не найден.")
    exit()

# Преобразуем стек в список для сортировки
coordinates_list = coordinate_stack.to_list()

# Выполняем быструю сортировку по x-координате
quick_sort(coordinates_list)

# Возвращаем отсортированные данные в стек
coordinate_stack.from_list(coordinates_list)

# Инициализируем бинарное дерево поиска
bst = BinarySearchTree()

# Записываем результат сортировки в бинарное дерево поиска
for x, y in coordinates_list:
    bst.insert(x, y)

# Инициализируем общий интеграл
total_integral = 0.0

# Проверяем, что в стеке достаточно элементов для интегрирования
if len(coordinate_stack) < 2:
    print("Недостаточно точек для интегрирования.")
else:
    # Получаем отсортированный список координат
    sorted_coordinates = bst.inorder_traversal()
    
    # Проходим по всем соседним парам точек
    for i in range(len(sorted_coordinates) - 1):
        # Получаем текущие точки
        x0, y0 = sorted_coordinates[i]
        x1, y1 = sorted_coordinates[i + 1]
        
        # Вычисляем интеграл на текущем интервале методом Симпсона
        integral = simpson_integration(x0, y0, x1, y1)
        
        # Добавляем к общему интегралу
        total_integral += integral

# Выводим результаты
print(f"Количество точек: {len(coordinate_stack)}")
print(f"Интеграл (метод Симпсона): {total_integral}")

# Выводим содержимое бинарного дерева поиска
print("\nБинарное дерево поиска содержит следующие координаты:")
bst.print_tree()

# Выводим отсортированные координаты
print("\nОтсортированные координаты:")
for i, (x, y) in enumerate(bst.inorder_traversal()):
    print(f"{i+1}: ({x}, {y})")