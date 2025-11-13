from Tokens import tokenize
from Reading import user_input, load_file
from Correctness_Check import correct_expression

def main():
    print("Выберите в каком формате работать с данными:\n"
      "\t1 - Ввод с клавиатуры\n"
      "\t2 - Загруженный файл")

    num = input("Введите номер формата: ")
    text = ""

    if num == '1':
        text = user_input()

    elif num == '2':
        filename = input("Введите имя файла: ")
        text = load_file(filename)
    else:
        print("Ошибка - выбранного варианта нет в перечне!")

    if not text:
        print("Нечего обрабатывать!")
        return
    tokens = tokenize(text)

    correct, message = correct_expression(tokens)
    print(message)

    show_tokens = input("Показывать токены? (y/n): ").lower() == 'y'
    if show_tokens:
        for token_type, value in tokens:
            print(f"{token_type:20} -> {value}")

if __name__ == "__main__":
    main()
