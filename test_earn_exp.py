from unittest import TestCase
import game


class TestEarnExp(TestCase):
    def test_earn_exp(self):
        char = game.make_character("Justin", 1, 0)
        minion = game.determine_enemy(char)
        actual = game.earn_exp(char, minion)
        expected = {'Attack': 60,
                    'Class': "Kog'maw",
                    'Current EXP': 100,
                    'Current HP': 65,
                    'Job': 'Ranger',
                    'Level': 1,
                    'Maximum EXP': 100,
                    'Maximum HP': 65,
                    'Name': 'Justin',
                    'Skill': 'Caustic Spittle',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        self.assertEqual(expected, actual)
