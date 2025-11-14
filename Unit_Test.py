import unittest
from Tokens import tokenize
from Correctness_Check import correct_expression


class TestTokenizer(unittest.TestCase):
    def sum(self):
        self.assertEqual(
            tokenize("2.5 + 3"),
            [('NUMBER', '2.5'), ('OPERATOR', '+'), ('NUMBER', '3.14')]
        )

    def degree(self):
        self.assertEqual(
            tokenize("-2 ** x1"),
            [('NUMBER', '-2'), ('OPERATOR', '**'), ('VARIABLE', 'x1')]
        )

    def constant(self):
        self.assertEqual(
            tokenize("pi + exp"),
            [('CONSTANT', 'pi'), ('OPERATOR', '+'), ('CONSTANT', 'exp')]
        )

    def expression(self):
        expr = "x // exp + y % 2 - z**2"
        tokens = tokenize(expr)
        self.assertEqual(
            tokens,
            [
                ('VARIABLE', 'x'), ('OPERATOR', '//'), ('CONSTANT', 'exp'),
                ('OPERATOR', '+'), ('VARIABLE', 'y'),
                ('OPERATOR', '%'), ('NUMBER', '2'),
                ('OPERATOR', '-'), ('VARIABLE', 'z'),
                ('OPERATOR', '**'), ('NUMBER', '2')
            ]
        )


class TestCorrectness(unittest.TestCase):
    def test1(self):
        expr = "x // exp + y % 2 - z**2"
        correct, _ = correct_expression(tokenize(expr))
        self.assertTrue(correct)

    def test2(self):
        correct, _ = correct_expression(tokenize("pi ** x = exp"))
        self.assertTrue(correct)

    def test3(self):
        correct, _ = correct_expression(tokenize("-(x + 3.1) * (exp - 1)"))
        self.assertTrue(correct)

    def test4(self):
        correct, _ = correct_expression(tokenize("x = 3 + 5"))
        self.assertTrue(correct)

    def test5(self):
        correct, message = correct_expression(tokenize("(y / 3"))
        self.assertFalse(correct)

    def test6(self):
        correct, message = correct_expression(tokenize("z % 3)"))
        self.assertFalse(correct)

    def test7(self):
        correct, _ = correct_expression(tokenize("2 / * 3"))
        self.assertFalse(correct)

    def test8(self):
        correct, _ = correct_expression(tokenize("2 3"))
        self.assertFalse(correct)

    def test9(self):
        correct, _ = correct_expression(tokenize("2 +"))
        self.assertFalse(correct)

    def test10(self):
        correct, _ = correct_expression(tokenize("x = y = z"))
        self.assertFalse(correct)


if __name__ == '__main__':
    unittest.main()
