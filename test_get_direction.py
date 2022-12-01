from unittest import TestCase
from unittest.mock import patch
from game import get_direction


class TestGetDirection(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_get_direction_lowest_number(self, _):
        actual = get_direction()
        expected = "1"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    def test_get_direction_highest_number(self, _):
        actual = get_direction()
        expected = "4"
        self.assertEqual(expected, actual)
