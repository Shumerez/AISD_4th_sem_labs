"""
Простой тест для проверки функциональности ЛР 5
"""
import sys
import os

# Добавляем путь к модулю
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Импортируем основные классы и функции из main.py
from main import Stack, quick_sort, simpson_integration, BinarySearchTree

def test_stack():
    """Тест стека"""
    print("Тестирование стека:")
    stack = Stack()
    
    # Тест пустого стека
    assert stack.is_empty() == True
    assert len(stack) == 0
    
    # Добавляем элементы
    stack.push((1, 1))
    stack.push((2, 4))
    stack.push((3, 9))
    
    assert len(stack) == 3
    assert stack.peek() == (3, 9)
    
    # Извлекаем элементы
    assert stack.pop() == (3, 9)
    assert stack.pop() == (2, 4)
    assert len(stack) == 1
    
    print("✓ Стек работает корректно")

def test_quick_sort():
    """Тест быстрой сортировки"""
    print("Тестирование быстрой сортировки:")
    
    # Тестовые данные
    data = [(3, 9), (1, 1), (4, 16), (2, 4)]
    expected = [(1, 1), (2, 4), (3, 9), (4, 16)]
    
    quick_sort(data)
    assert data == expected
    
    print("✓ Быстрая сортировка работает корректно")

def test_simpson_integration():
    """Тест интегрирования методом Симпсона"""
    print("Тестирование интегрирования методом Симпсона:")
    
    # Простой тест: интеграл линейной функции y = x на [0, 2] должен быть 2
    result = simpson_integration(0, 0, 2, 2)
    expected = 2.0
    assert abs(result - expected) < 0.0001
    
    print("✓ Интегрирование методом Симпсона работает корректно")

def test_bst():
    """Тест бинарного дерева поиска"""
    print("Тестирование бинарного дерева поиска:")
    
    bst = BinarySearchTree()
    
    # Добавляем элементы
    bst.insert(3, 9)
    bst.insert(1, 1)
    bst.insert(4, 16)
    bst.insert(2, 4)
    
    # Проверяем обход в порядке возрастания
    result = bst.inorder_traversal()
    expected = [(1, 1), (2, 4), (3, 9), (4, 16)]
    assert result == expected
    
    print("✓ Бинарное дерево поиска работает корректно")

if __name__ == "__main__":
    print("Запуск тестов для ЛР 5...\n")
    
    test_stack()
    test_quick_sort()
    test_simpson_integration()
    test_bst()
    
    print("\n✅ Все тесты прошли успешно!")