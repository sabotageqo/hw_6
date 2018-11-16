from input_var import var_input
from operation import OPERATION
from help_for_use import help_in_proggram


def main():
    print('{:-^67}'.format(" Вы зашли в калькулятор! "))
    loop = True
    while loop:
        print(' {:^67}'.format("Меню: "))
        print('{} {}'.format(1, "Ввести значения и посчитать"))
        print('{} {}'.format(2, "Помощь в использовании калькулятором"))
        print('{} {}'.format(3, "Выйти"))
        print()
        try:
            response = int(input('Выберите пункт: '))
            print()
            if response == 1:
                try:
                    res = None
                    input_some_var = var_input()
                    res = OPERATION[input_some_var["operation"]](input_some_var["first_var"], input_some_var["second_var"])
                    print("Ответ: ", res)
                    print()
                except (ValueError, ZeroDivisionError) as error:
                    print("Ошибка: ", error)
                    print("Попробуйте еще раз!")
                    print()
                except KeyError:
                    print("Ошибка : операции = '{}', нету в программе".format(input_some_var["operation"]))
                    print("Попробуйте еще раз!")
                    print()
            elif response == 2:
                print(help_in_proggram.__doc__)
            elif response == 3:
                print("Вы вышли из программы. Хорошего времени суток!")
                loop = False
            else:
                print("В меню нету такого пункта = '{}', выберите пункт, который есть в меню".format((response)))
                print()
        except ValueError as mistake:
            print("Ошибка: ", mistake)
            print("Неправильный ввод, попробуйте еще раз")
            print()


main()