from unittest import TestCase
from unittest.mock import patch
import game


class TestCheckForEnemies(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_check_for_enemies_true(self, _):
        char = game.make_character("Justin", 1, 0)
        actual = game.check_for_enemies(char)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[3])
    def test_check_for_enemies_false(self, _):
        char = game.make_character("Justin", 1, 0)
        actual = game.check_for_enemies(char)
        expected = False
        self.assertEqual(expected, actual)

