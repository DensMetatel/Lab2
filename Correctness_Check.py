# Проверяет на корректность список токенов математического выражения
def correct_expression(tokens):
    if not tokens:
        return False, "Выражение пустое!"

    left_and_right_count = 0
    last_type = None
    equal_count = 0

    for token_type, value in tokens:
        if token_type == "OPERATOR" and value == "=":
            equal_count += 1
            if equal_count > 1:
                return False, "Более одного знака '='!"
            if last_type == "OPERATOR":
                return False, "'=' не может идти после оператора!"

        if token_type == "LEFT_BRACKET":
            left_and_right_count += 1
        elif token_type == "RIGHT_BRACKET":
            left_and_right_count -= 1
            if left_and_right_count < 0:
                return False, "Лишняя закрывающая скобка!"

        if last_type:
            if last_type == "NUMBER" and token_type == "NUMBER":
                return False, "Отсутствует оператор между числами!"
            if last_type == "OPERATOR" and token_type == "OPERATOR" and value != "=":
                return False, "Два оператора подряд!"

        last_type = token_type

    if left_and_right_count != 0:
        return False, "Нарушен баланс скобок!"

    if tokens[-1][0] == "OPERATORS" and tokens[-1][1] != "=":
        return False, "Выражение не может заканчиваться оператором!"

    return True, 'Выражение "синтаксически" корректно'
