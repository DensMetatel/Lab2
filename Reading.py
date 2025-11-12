import requests

# Пользовательский ввод
def user_input():
    return input("Введите математическое выражение: ")

# Поиск информации на веб-странице по URL
def web_page_by_url(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException as object_mistake:
        print(f"Ошибка при запросе к {url}: {object_mistake}")
        return ""

# Поиск информации в загруженном файле
def load_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"{filename} не найден!")
        return ""

