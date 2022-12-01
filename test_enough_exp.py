from unittest import TestCase
import game


class TestEnoughExp(TestCase):
    def test_enough_exp_more_max_exp(self):
        char = game.make_character("Justin", 1, 0)
        expected = game.enough_exp(char)
        actual = False
        self.assertEqual(expected, actual)

    def test_enough_exp_same_max_current_exp(self):
        char = game.make_character("Justin", 1, 0)
        char['Current EXP'] = 100
        expected = game.enough_exp(char)
        actual = True
        self.assertEqual(expected, actual)

    def test_enough_exp_more_current_exp(self):
        char = game.make_character("Justin", 1, 0)
        char['Current EXP'] = 150
        expected = game.enough_exp(char)
        actual = True
        self.assertEqual(expected, actual)
