    if not testing_mode:
        try:
            # Ввод переменных. 
            # float a - коэффициент при x^2
            # float b - коэффициент при x^1
            # float c - коэффициент при x^0
                a, b, c = map(float, input("Введите коэффициенты квадратного уравнения, начиная с коэффициента при x^2 (a b c):\n>>> ").split())
        except ValueError:
            print("Введите число, будьте человеком") if not testing_mode else False 
            exit()