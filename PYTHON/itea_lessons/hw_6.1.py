from string import whitespace
text = "fiwufwehfiuwh uihwefiuhweiufd"
def string_processing(string):
    result = ("{} подходит под условие задачи".format(text))
    if list(set(whitespace) & set(text)):
        raise ValueError("содержит непечатные символы")
    return result
try:
    print(string_processing(text))
except ValueError as e:
    print("Проблема в том, что: ", text, e)
