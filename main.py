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



