from unittest import TestCase
from unittest.mock import patch
from game import get_character_class


class TestGetCharacterClass(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_get_character_class(self, _):
        actual = get_character_class()
        expected = 0
        self.assertEqual(expected, actual)
