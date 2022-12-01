from unittest import TestCase
import game


class TestLevelUp(TestCase):
    def test_level_up_level_one(self):
        char = game.make_character("Justin", 1, 0)
        char["X-coordinate"] = 2
        char["Y-coordinate"] = 3
        char["Current EXP"] = 100
        expected = {'Attack': 90,
                    'Class': "Kog'maw",
                    'Current EXP': 0,
                    'Current HP': 150,
                    'Job': 'SharpShooter',
                    'Level': 2,
                    'Maximum EXP': 150,
                    'Maximum HP': 150,
                    'Name': 'Justin',
                    'Skill': 'Bio-Arcane Barrage',
                    'X-coordinate': 2,
                    'Y-coordinate': 3}
        actual = game.level_up(char, 0)
        self.assertEqual(expected, actual)

    def test_level_up_level_two(self):
        char = game.make_character("Justin", 2, 0)
        char["X-coordinate"] = 2
        char["Y-coordinate"] = 3
        char["Current EXP"] = 100
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
                    'X-coordinate': 2,
                    'Y-coordinate': 3}
        actual = game.level_up(char, 0)
        self.assertEqual(expected, actual)
