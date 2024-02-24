import math

def tetra_solve(a = 'error', b = 'error', c = 'error', testing_mode = False):
    if not testing_mode:
        try:
            # Ввод переменных. 
            # float a - коэффициент при x^2
            # float b - коэффициент при x^1
            # float c - коэффициент при x^0
            a, b, c = map(float, input("Введите коэффициенты квадратного уравнения, начиная с коэффициента при x^2 (a b c):\n>>> ").split())
        except ValueError:
            print("Введите число, будьте человеком") if not testing_mode else False 
            return False

    if (a == 0):
        if (b == 0):
            if (c == 0):
                # Случай a == 0 И b == 0 И с == 0.
                # Если все коэффициенты == 0, то уравнение обращается в 
                # 0 = 0
                # Следовательно, уравнение верно при любых x
                print("x - любое") if not testing_mode else False
                return True
            else:
                # Случай a == 0 И b == 0 И с != 0.
                # Если коэффициенты при x == 0, а c != 0, то уравнение обращается в 
                # с = 0, где с != 0
                # Следовательно, уравнение ложно при любых x
                print("нет корней") if not testing_mode else False
                return {}
        else:
            # Случай a == 0 И b != 0 И с - любое
            # Если коэффициент при x^2 == 0, а b != 0, то уравнение обращается в линейное
            # bx + c = 0, где b != 0
            # Следовательно, решим линейное уравнение с помощью формулы
            # x =  -c / b
            print("уравнение обращается в линейное") if not testing_mode else False
            x = -c / b
            print("%.4f" % x) if not testing_mode else False
            return {x}
    else:
        # Случай a != 0 И b,c - любые
        # Если коэффициент при x^2 != 0, то уравнение является квадратным.
        # Определим количество и вид его корней через формулу дискриминанта 
        # D = b*b + (-4) * a * c

        D = (b*b) + ((-4) * a * c) # float D - дискриминант квадратного уравнения

        if D > 0:
            # Случай D > 0
            # Если дискриминант больше нуля, то квадратное уравнение имеет два различных действительных корня
            # Обозначим их как x1 и x2
            # И найдем по стандартным формулам для корней квадратного уравнения, представленным ниже
            x1 = ( -b + math.sqrt(D) ) / (2*a) # float x1 - первый корень квадратного уравнения
            x2 = ( -b - math.sqrt(D) ) / (2*a) # float x2 - второй корень квадратного уравнения
            print("D > 0") if not testing_mode else False
            print("%.4f" % x1) if not testing_mode else False
            print("%.4f" % x2) if not testing_mode else False
            return {x1, x2}
        elif D == 0:
            # Случай D == 0
            # Если дискриминант равен нулю, то квадратное уравнение имеет два кратных (одинаковых) действительных корня
            # Обозначим их как x1 = x2 = x
            # И найдем по стандартной формуле для кратных корней квадратного уравнения, представленной ниже
            print("D == 0") if not testing_mode else False
            x = (-b) / (2*a)
            print("%.4f" % x) if not testing_mode else False
            return {x}
        elif D < 0:
            # Случай D < 0
            # Если дискриминант меньше нуля, то квадратное уравнение имеет два мнимых корня
            # В рамках нашего алгоритма мы не занимаемся их вычислением
            # И найдем по стандартной формуле для кратных корней квадратного уравнения, представленной ниже
            print('a > 10') if not testing_mode else False
            print("нет действительных корней") if not testing_mode else False
            return {}


mode = input("Какой режим запуска? (run [T]ests / run [M]anually)")   
if mode == 'M':
    while True:
    # функция вычисления корня будет автоматически запускаться заново после конца текущего вызова
        tetra_solve()

elif mode == 'T':
    # Семь тестов
    # 1 Неверные входные данные
# TODO !!!
    # Случай D > 0
    # Если дискриминант больше нуля, то квадратное уравнение имеет два различных действительных корня
    # Обозначим их как x1 и x2
    # И найдем по стандартным формулам для корней квадратного уравнения, представленным ниже
    assert {} == tetra_solve(3, -4, 94, testing_mode = True)
    print("Тест D > 0 успешен")

    # Случай D == 0
    # Если дискриминант равен нулю, то квадратное уравнение имеет два кратных (одинаковых) действительных корня
    # Обозначим их как x1 = x2 = x
    # И найдем по стандартной формуле для кратных корней квадратного уравнения, представленной ниже
    assert {3.5} == tetra_solve(-4, 28, -49, testing_mode = True)
    print("Тест D == 0 успешен")

    # Случай D < 0
    # Если дискриминант меньше нуля, то квадратное уравнение имеет два мнимых корня
    # В рамках нашего алгоритма мы не занимаемся их вычислением
    # И найдем по стандартной формуле для кратных корней квадратного уравнения, представленной ниже
    assert {3, -3} == tetra_solve(-6, 0, 54, testing_mode = True)
    print("Тест D < 0 успешен")

    # Случай a == 0 И b == 0 И с == 0.
    # Если все коэффициенты == 0, то уравнение обращается в 
    # 0 = 0
    # Следовательно, уравнение верно при любых x
    assert True == tetra_solve(0, 0, 0, testing_mode = True)
    print("Тест a = 0, b = 0, c = 0 успешен")

    # Случай a == 0 И b == 0 И с != 0.
    # Если коэффициенты при x == 0, а c != 0, то уравнение обращается в 
    # с = 0, где с != 0
    # Следовательно, уравнение ложно при любых x
    assert {} == tetra_solve(0, 0, 4, testing_mode = True)
    print("Тест a == 0, b == 0, с != 0 успешен")

    # Случай a == 0 И b != 0 И с - любое
    # Если коэффициент при x^2 == 0, а b != 0, то уравнение обращается в линейное
    # bx + c = 0, где b != 0
    # Следовательно, решим линейное уравнение с помощью формулы
    # x =  -c / b
    assert {-2} == tetra_solve(0, 4, 8, testing_mode = True)
    print("Тест линейного уравнения успешен")
else:
    print("Нет такого режима")