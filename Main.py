from Tokens import tokenize
from Reading import user_input, web_page_by_url, load_file

print("Выберите в каком формате работать с данными:\n"
      "\t1 - Ввод с клавиатуры\n"
      "\t2 - Web-страница\n"
      "\t3 - Загруженный файл")

num = input("Введите номер формата: ")

match num:
    case '1':
        text = user_input()
    case '2':
        filename = input("Введите URL: ")
        text = web_page_by_url(filename)
    case '3':
        filename = input("Введите имя файла: ")
        text = load_file(filename)
    case _:
        text = ''
        print("Ошибка - выбранного варианта нет в перечне!")

if text:
    tokens = tokenize(text)
    for token_type, value in tokens:
        print(f"{token_type:20} -> {value}")