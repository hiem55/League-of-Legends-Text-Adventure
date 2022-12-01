from unittest import TestCase
import game


class TestHealPlayer(TestCase):
    def test_heal_player(self):
        char = game.make_character("Justin", 3, 0)
        char["Current HP"] = 50
        actual = game.heal_player(char)
        expected = {'Attack': 115,
                    'Class': "Kog'maw",
                    'Current EXP': 0,
                    'Current HP': 230,
                    'Job': 'ADC',
                    'Level': 3,
                    'Maximum EXP': 100000,
                    'Maximum HP': 230,
                    'Name': 'Justin',
                    'Skill': 'Living Artillery',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        self.assertEqual(expected, actual)
