# Пользовательский ввод
def user_input():
    return input("Введите математическое выражение: ")

# Поиск информации в загруженном файле
def load_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"{filename} не найден!")
        return ""
