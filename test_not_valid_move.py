from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestNotValidMove(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_not_valid_move(self, mock_stdout):
        char = game.make_character("Justin", 1, 0)
        game.not_valid_move(char)
        expected = "\nSorry Justin, you can't go in that direction. Choose a different direction.\n"
        self.assertEqual(expected, mock_stdout.getvalue())
