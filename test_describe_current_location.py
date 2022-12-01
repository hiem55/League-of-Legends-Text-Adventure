from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_stdout):
        new_map = game.make_board(2, 2)
        char = game.make_character("Justin", 1, 0)
        new_map[(0, 0)] = "Demacia"
        game.describe_current_location(new_map, char)
        expected = "You are in (Demacia)\n"
        self.assertEqual(expected, mock_stdout.getvalue())
