'''Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять
✔ Сумма пополнения и снятия кратны 50 у.
✔ Процент за снятие — 1.5% от суммы снят
✔ После каждой третей операции пополне
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычита
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

summ_card = 0
n = input('Введите 1 - пополнить счет, 2 - снять деньги, 3 - выход')


def operation(n, summ_card):
    print(n)

    while True:
        match n:
            case "1":
                while True:
                    popolnen = int(input('Введите сумму пополнения, кратную 50 :'))
                    cratn = popolnen % 50
                    if cratn == 0:
                        summ_card += popolnen
                        print (summ_card)

                    else:
                        print('Вы ввели сумму не кратную 50')
                        break


            case 2:
                sn = int(input('Введите сумму снятия, кратную 50 :'))
                cratn = sn % 50
                if cratn == 0:
                    summ_card -= sn
                else:
                    print('Вы ввели сумму не кратную 50')

            case 3:
                break

        return summ_card


operation(n, summ_card)
print(summ_card)
while True:
    qw = int(input('Для продолжения операций нажните 1, для выхода 0 '))
    if qw == 1:
        n = input('Введите 1 - пополнить счет, 2 - снять деньги, 3 - выход')
        operation(n, summ_card)
    else: print(summ_card)


    print(summ_card)
