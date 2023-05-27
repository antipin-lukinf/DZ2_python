# создать несколько переменных и проверить их тип


# a = 1
# b = 'строка'
# c = 0.1
# d = (1, 1)
# e = {1: 3}
#
# print(f'a - {type(a)}, b - {type(b)}, c - {type(c)}, d - {type(d)}, e - {type(e)}')
#
# # создайте в переменной data список значений разных типов, перечислив их через запятую, внутри квадратных скобок
#
# data = [a, b, c, d, 1, "строка"]
# for i, el in enumerate(data, start=1):
#     print(i, el, id(el), el.__sizeof__(), hash(el))
#     if isinstance(el, int):
#         print('это целое число')
#     elif isinstance(el, str):
#         print('это строка')


# написать программу которая получает целое число и возвращает его двоичное, восмеричное строковое представление

def task3(num: int, mode: str) -> str:
    result = ''
    convert: int = 2
    match mode:
        case "bin":
            convert = 2
        case "bin":
            convert = 8
    while num >= 1:
        res = num % convert

        result += str(res)
        num = num // convert

    return result[::-1]


print(task3(21, mode="bin"), f"assert: {bin(21)}")
print(task3(21, mode="oct"), f"assert: {oct(21)}")

# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой


import math
import decimal


def circle(d: decimal) -> tuple[decimal, decimal]:
    decimal.getcontext().prec = 42
    _pi = decimal.Decimal(math.pi)
    if d <= 1000:
        s = (_pi * d ** 2) / 4
        l = _pi * d

    return decimal.Decimal(s), decimal.Decimal(l)


print(circle(decimal.Decimal(34)))


'''
Задание №5
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня

ax2 + bx + c = 0, где коэффициенты a, b и c — произвольные числа, причем a ≠ 0.
Пусть дано квадратное уравнение ax2 + bx + c = 0. Тогда дискриминант — это просто число D = b2 − 4ac.
'''

a = int(input('Введите коэффициент a не равный 0 :'))
b = int(input('Введите коэффициент b :'))
c = int(input('Введите коэффициент c :'))

d = b**2 - 4 * a * c
print(d)

if d == 0:
    x = (-b) / 2 * a
    print(x)
else:
    d = abs(d)
    x1 = (-b - math.sqrt(d)) / 2 * a
    x2 = (-b + math.sqrt(d)) / 2 * a
    print(x1)
    print(x2)




