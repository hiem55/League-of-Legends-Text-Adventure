from unittest import TestCase
from unittest.mock import patch
import game
import io


class TestCreateMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_map(self, mock_stdout):
        new_map = game.make_board(2, 2)
        char = game.make_character("Justin", 1, 0)
        game.create_map(new_map, char)
        expected = "[x][ ]\n[ ][Y]\n"
        self.assertEqual(expected, mock_stdout.getvalue())
