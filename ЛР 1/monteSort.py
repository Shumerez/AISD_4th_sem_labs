import random

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

def sortMonteCarlo(input_filename = filenameForTest3, output_filename = filenameOutput, testing_mode = False):
	# Float List numbers - Массив, в котором содержатся сортируемые числа в ходе работы программы
	numbers = []
	# Ввод из файла
	with open(input_filename, 'r') as file:
		# String List content - относительный путь к файлу с входными данными
		content = file.read().splitlines()

	# Конвертация полученного массива строк в массив чисел типа float
	for str_number in content:
		try:
			numbers.append(float(str_number))

		# Обработка случая, когда в файле предоставлены не float
		except ValueError:
			print("ОШИБКА: Файл содержит данные, не приводимые к типу float")
			return

		# Обработка случая, когда в файле предоставлены числа, большие float
		if (float(str_number) == float(str_number) + 1): # raise OverflowError() - имеется в виду обработка этого исключения
			print("ОШИБКА: Файл содержит числа, превышающие размер типа данных float")
			return

	# Сортировка

	# Цикл проверки массива на отсортированность
	while not isSorted(numbers):
		# "Сортировка" массива методом Монте-Карло 
		random.shuffle(numbers)

	# Запись в файл
	with open(output_filename, 'w') as file:
		for i in range(len(numbers)):
			file.write(str(numbers[i]) + '\n')

	print(numbers) # НЕ отладочный вывод результата работы в stdout
	return

# Небольшая функция, проверяющая сортировку массива за O(N)
def isSorted(array):
	for i in range(len(array) - 1):
		if array[i] < array[i + 1]:
			return False
	return True

mode = input("Какой режим запуска? (run [T]ests / run [M]anually)")   
if mode == 'M':
	while True:
		# функция сортировки массива будет запускаться заново при каждом нажатии Enter, 
		# между итерациями можно менять файл с входными данными
		sortMonteCarlo()
		input("")

elif mode == 'T':
	# Три теста
	# Тест 1: Случай со строковыми данными в файле

	print("\nТест 1: Не-float данныe в файле")
	print("Содержимое файла " + filenameForTest1)
	with open(filenameForTest1, 'r') as file:
		print(file.read())
	print("\nВывод программы:")
	sortMonteCarlo(input_filename = filenameForTest1, testing_mode = True)

	# Тест 2: Случай с переполнением типа данных float
	print("\nТест 2: float в файле выходит за размер типа данных")
	print("Содержимое файла " + filenameForTest2)
	with open(filenameForTest2, 'r') as file:
		print(file.read())
	print("\nВывод программы:")
	sortMonteCarlo(input_filename = filenameForTest2, testing_mode = True)

	# Тест 3: Случай с валидным файлом
	print("\nТест 3: Валидный файл ввода: дробные числа, положительные числа, отрицательные числа, ноль.")
	print("Содержимое файла " + filenameForTest3)
	with open(filenameForTest3, 'r') as file:
		print(file.read())
	print("\nВывод программы:")
	sortMonteCarlo(input_filename = filenameForTest3, testing_mode = True)

else:
	print("Вы ввели некорректный режим запуска. Введите T (для запуска тестов) или M (для запуска в ручном режиме)")



