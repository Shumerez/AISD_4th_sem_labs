import random

# Объявление переменных
# String input_filename - относительный путь к файлу с входными данными
# String output_filename - относительный путь к файлу для записи результата сортировки
# Float Array array - Массив, в котором содержатся сортируемые числа в ходе работы программы
input_filename = "numbers.txt"
output_filename = "sorted_numbers.txt"
array = []

def sortMonteCarlo(array, input_filename = 'numbers.txt', output_filename = "sorted_numbers.txt"):
	# Ввод из файла
	with open(input_filename, 'r') as file:
		# String Array content - относительный путь к файлу с входными данными
		content = file.read().splitlines()

	# Конвертация полученного массива строк в массив float-ов
	for str_number in content:
	    array.append(float(str_number))

	# Сортировка
	# установка условия проверки отсортированности массива.
	# Float Array theGoal - Отсортированный массив, который используется для проверки успешности работы метода Монте-Карло
	theGoal = sorted(array, reverse=True) 

	# Цикл проверки массива на отсортированность
	while theGoal != array:
		# "Сортировка" массива методом Монте-Карло 
		random.shuffle(array)

	# Запись в файл
	with open(output_filename, 'w') as file:
		for i in range(len(array)):
			file.write(str(array[i]) + '\n')

	# Вывод в stdout
	return array


print(sortMonteCarlo(array))
input("")   