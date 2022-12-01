from unittest import TestCase
from unittest.mock import patch
from game import get_character_name


class TestGetCharacterName(TestCase):
    @patch('builtins.input', side_effect=["Justin"])
    def test_get_character_name(self, _):
        actual = get_character_name()
        expected = "Justin"
        self.assertEqual(expected, actual)
