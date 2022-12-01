from unittest import TestCase
from unittest.mock import patch
from game import get_battle_choice


class TestGetBattleChoice(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_get_battle_choice(self, _):
        actual = get_battle_choice()
        expected = 1
        self.assertEqual(expected, actual)
