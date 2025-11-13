# Проверяет корректность списка токенов математического выражения
def correct_expression(tokens):
    if not tokens:
        return False, "Выражение пустое!"

    left_and_right_count = 0
    last_type = None

    for token_type, value in tokens:
        if token_type == "LEFT_BRACKET":
            left_and_right_count += 1
        elif token_type == "RIGHT_BRACKET":
            left_and_right_count -= 1
            if left_and_right_count < 0:
                return False, "Лишняя закрывающая скобка!"

        if last_type:
            if last_type == "NUMBER" and token_type == "NUMBER":
                return False, "Отсутствует оператор между числами!"
            if last_type == "OPERATORS" and token_type == "OPERATORS":
                return False, "Два оператора подряд!"

        last_type = token_type

    if left_and_right_count != 0:
        return False, "Баланс скобок нарушен!"

    if tokens[-1][0] == "OPERATOR":
        return False, "Выражение не может заканчиваться оператором!"

    return True, "Выражение корректно"
