import numpy as np
import numpy.polynomial.legendre as leg

# Определяем функцию, которую будем интегрировать
def func(x):
    return np.exp(-x**2)

# Заданные координаты точек (узлов)
nodes = np.array([-0.7745966692, 0, 0.7745966692])

# Рассчитываем веса для заданных узлов
# Используем полином Лежандра для расчета весов
n = len(nodes)
weights = 2 / ( ( 1 - nodes**2 ) * (leg.legval(nodes, leg.legder([0]*n + [1])) )**2 )

# Вычисляем интеграл
integral = np.sum(weights * func(nodes))

print(f"Значение интеграла: {integral}")