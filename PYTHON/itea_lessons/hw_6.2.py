from string import whitespace

text = "!My name_is_George!"

class WhitespaceError(Exception):
    def __init__(self, position, symbol):
        self.position = position
        self.symbol = symbol


def string_processing(text, *args, **kwargs):
    result = "sabotage " + text.upper() * 3 + " hello"

    for sym in text:
        if sym in whitespace:
            raise WhitespaceError(text.find(sym) + 1, repr(sym))
    return result


def main():

    try:
        result = string_processing(text, whitespace)
        print("Ваш текст для названия:", result)
    except WhitespaceError as e:
        print("Обнаружен исключённый символ, он находится под номером {}, а его репрезентация - {}".format(e.position, e.symbol))

if __name__ == "__main__":
    main()
