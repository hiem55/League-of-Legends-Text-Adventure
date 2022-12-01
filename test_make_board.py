from unittest import TestCase
from unittest.mock import patch
from game import make_board


class TestMakeBoard(TestCase):
    @patch('random.choice', side_effect=["Demacia"])
    def test_make_board(self, _):
        actual = make_board(1, 1)
        expected = {(0, 0): "Demacia"}
        self.assertEqual(expected, actual)
