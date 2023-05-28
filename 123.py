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

# summ_card = 0
# n = input('Введите 1 - пополнить счет, 2 - снять деньги, 3 - выход')
#
#
# def operation(n, summ_card):
#     print(n)
#
#     while True:
#         match n:
#             case "1":
#                 while True:
#                     popolnen = int(input('Введите сумму пополнения, кратную 50 :'))
#                     cratn = popolnen % 50
#                     if cratn == 0:
#                         summ_card += popolnen
#                         print (summ_card)
#
#                     else:
#                         print('Вы ввели сумму не кратную 50')
#                         break
#
#
#             case 2:
#                 sn = int(input('Введите сумму снятия, кратную 50 :'))
#                 cratn = sn % 50
#                 if cratn == 0:
#                     summ_card -= sn
#                 else:
#                     print('Вы ввели сумму не кратную 50')
#
#             case 3:
#                 break
#
#         return summ_card
#
#
# operation(n, summ_card)
# print(summ_card)
# while True:
#     qw = int(input('Для продолжения операций нажните 1, для выхода 0 '))
#     if qw == 1:
#         n = input('Введите 1 - пополнить счет, 2 - снять деньги, 3 - выход')
#         operation(n, summ_card)
#     else: print(summ_card)
#
#
#     print(summ_card)

class Bank:

    _BALANCE = 0
    _MIN = 50
    _COMMISSION = 0.015
    _BONUS = 0.03
    _TAX = 0.10
    _OPERATION: int

    def __init__(self):
        self._OPERATION = 0


    def _in(self, cash: int)-> tuple[int, int] | None:
        if cash % self._MIN == 0:
            self._BALANCE += cash
            self._OPERATION += 1
            return  self._BALANCE, self._OPERATION
        else:
            return None

    def _out(self, cash: int, commission: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0 and self._BALANCE > 0 and self._BALANCE - (cash + commission) >= 0:
            self._BALANCE -= cash
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _check_commission(self, cash: int) -> int:
        sum_commission = cash * self._COMMISSION
        _MAX = 600
        _MIN = 30

        if sum_commission > _MAX:
            return _MAX
        elif sum_commission < _MIN:
            return _MIN
        else:
            return  int(sum_commission)


    def _exit(self):
        return "Пока"

    def _check_operation(self):
        return (False, True)[self._OPERATION % 3 == 0]

    def start(self, mode: str, cash: int = 0) -> str:

        check_operation = self._check_operation()
        if check_operation:
            self._BALANCE += self._BALANCE * self._BONUS



        match mode:
            case "in":
                data = self._in(cash=cash)

                com_data = self._check_commission(cash=cash)

                return f"Средства были зачислены сумма: {cash}, баланс: {self._BALANCE}"

            case "out":
                com_data = self._check_commission(cash=cash)

                data = self._out(cash=cash, commission=com_data)

                if data:
                    return f"Операция осуществлена успешна, сумма: {cash}, коммисия: {com_data}, баланс: {self._BALANCE}"
                else:
                    return  "Не хватает средств"




            case "exit":
                return self._exit()

client = Bank()
print(client.start(mode="in", cash=100))


























