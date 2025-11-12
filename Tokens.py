import re

# Шаблоны токенов
Patterns = re.compile(
    r"""
    (?P<NUMBER>-?\d+(\.\d+)?)   |
    (?P<OPERATORS>[+\-*/])      |
    (?P<LEFT_BRACKET>\()        |
    (?P<RIGHT_BRACKET>\))       |
    (?P<SPACE>\s+)
    """, re.VERBOSE
)

# Разбиение математического выражения на токены
def tokenize(text):
    tokens = []
    for match in Patterns.finditer(text):
        if match.lastgroup == "SPACE":
            continue
        tokens.append((match.lastgroup, match.group()))
    return tokens