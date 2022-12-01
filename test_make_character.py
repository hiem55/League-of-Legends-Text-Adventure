from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_lowest_level(self):
        actual = make_character("Justin", 1, 0)
        expected = {'Attack': 60,
                    'Class': "Kog'maw",
                    'Current EXP': 0,
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

    def test_make_character_highest_level(self):
        actual = make_character("Justin", 3, 0)
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

    def test_make_character_lowest_level_class_one(self):
        actual = make_character("Justin", 1, 1)
        expected = {'Attack': 65,
                    'Class': 'Irelia',
                    'Current EXP': 0,
                    'Current HP': 80,
                    'Job': 'Warrior',
                    'Level': 1,
                    'Maximum EXP': 100,
                    'Maximum HP': 80,
                    'Name': 'Justin',
                    'Skill': 'Bladesurge',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        self.assertEqual(expected, actual)

    def test_make_character_lowest_level_class_two(self):
        actual = make_character("Justin", 1, 2)
        expected = {'Attack': 30,
                    'Class': 'Ornn',
                    'Current EXP': 0,
                    'Current HP': 150,
                    'Job': 'Meat Shield',
                    'Level': 1,
                    'Maximum EXP': 100,
                    'Maximum HP': 150,
                    'Name': 'Justin',
                    'Skill': 'Volcanic Rupture',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        self.assertEqual(expected, actual)

    def test_make_character_lowest_level_class_three(self):
        actual = make_character("Justin", 1, 3)
        expected = {'Attack': 65,
                    'Class': 'Syndra',
                    'Current EXP': 0,
                    'Current HP': 60,
                    'Job': 'Mage',
                    'Level': 1,
                    'Maximum EXP': 100,
                    'Maximum HP': 60,
                    'Name': 'Justin',
                    'Skill': 'Dark Sphere',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        self.assertEqual(expected, actual)

    def test_make_character_level_two_class_three(self):
        actual = make_character("Justin", 2, 3)
        expected = {'Attack': 95,
                    'Class': 'Syndra',
                    'Current EXP': 0,
                    'Current HP': 140,
                    'Job': 'Sorcerer',
                    'Level': 2,
                    'Maximum EXP': 150,
                    'Maximum HP': 140,
                    'Name': 'Justin',
                    'Skill': 'Scatter the Weak',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        self.assertEqual(expected, actual)
