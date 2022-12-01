from unittest import TestCase
from unittest.mock import patch
from game import display_character_class
import io


class TestDisplayCharacterClass(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_class(self, mock_stdout):
        display_character_class()
        expected = ("1. Kog'maw:  Low HP but Strong Attack Damage Carry\n"
                    "2. Irelia:  Balanced Melee Fighter\n"
                    "3. Ornn:  High HP but Low Attack\n"
                    "4. Syndra:  Low HP but Strong Attack Mage\n")
        self.assertEqual(mock_stdout.getvalue(), expected)
