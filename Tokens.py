import re

# Шаблоны токенов
Patterns = re.compile(
    r"""
    (?P<NUMBER>-?\d+(\.\d+)?)               |
    (?P<OPERATOR>\*\*|//|\+|-|/|%|\*|=)  |
    (?P<LEFT_BRACKET>\()                    |
    (?P<RIGHT_BRACKET>\))                   |
    (?P<CONSTANT>pi|exp)                    |
    (?P<VARIABLE>[a-zA-Z_]\w*)
    """, re.VERBOSE
)

# Разбиение математического выражения на токены
def tokenize(text):
    tokens = []
    for match in Patterns.finditer(text):
        tokens.append((match.lastgroup, match.group()))
    return tokens

