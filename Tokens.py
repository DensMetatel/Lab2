import re

Patterns = re.compile(
    r"""
    (?P<NUMBER>-?\d+(\.\d+)?)   |
    (?P<OPERATORS>[+\-*/])      |
    (?P<LEFT_BRACKET>\()        |
    (?P<RIGHT_BRACKET>\))
    """, re.VERBOSE
)
