

class TooManyTypes(Exception):
    def __init__(self, type_set):
        self.type_set = type_set

def check_params_type(*args):
    type_set = set()
    for gum in args:
        type_set.add(type(gum))
    if len(type_set) > 1:
        raise TooManyTypes(type_set)
    else:
        print("Все аргументы успешно стали операторами функции!")
    return type_set



def main(*args):
    try:
        check_params_type(*args)
    except TooManyTypes as e:
        print("Данные элементы, не подходят, так как они относятся к разным типам, список: {}.".format(e.type_set))
    finally:
        for gum in args:
            print("Элемент '{}' относится к типу {}.".format(gum, type(gum)))


if __name__ == "__main__":
    main(1,"hellos","george",56.745,(90,54),"kiany_rivz")