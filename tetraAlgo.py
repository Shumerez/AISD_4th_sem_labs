# ax^2 + bx + c = 0

# x1 = ( -b + sqrt(D) ) / 2a
# x2 = ( -b - sqrt(D) ) / 2a

import math

a, b, c = map(float, input("Входные данные пожалуйста (три числа, разделены пробелами)\n>>> ").split())

if type(a) != float:
	print("Введите число")
	exit()

if (a == 0 and b != 0):
	print("уравнение обращается в линейное")
	x = -c/b
	print(x)
	exit()

if (a == 0 and b == 0):
	print("нет решений")
	exit()
	

D = b*b + (-4)*a*c

if D > 0:
	x1 = ( -b + math.sqrt(D) ) / (2*a)
	x2 = ( -b - math.sqrt(D) ) / (2*a)
	print("D > 0")
	print(x1)
	print(x2)
elif D == 0:
	print("D == 0")
	x = -1*b  / (2*a)
	print(x)
elif D < 0:
	print("D < 0")
	print("нет решений")
else:
	print("Непредвиденная ошибка")