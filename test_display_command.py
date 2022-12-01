from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestDisplayCommand(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_command(self, mock_stdout):
        char = game.make_character("Justin", 1, 0)
        game.display_command(char)
        expected = 'Justin, enter your next move: \n [1]. Attack\n [2]. Run Away\n'
        self.assertEqual(expected, mock_stdout.getvalue())

