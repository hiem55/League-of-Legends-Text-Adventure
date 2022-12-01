from unittest import TestCase
from game import make_character
from game import determine_enemy


class TestDetermineEnemy(TestCase):
    def test_determine_enemy_level_one(self):
        char = make_character("Justin", 1, 0)
        actual = determine_enemy(char)
        expected = {'ATTACK': 10,
                    'EXP': 100,
                    'HP': 100,
                    'MAXIMUM_HP': 100,
                    'NAME': 'Elise',
                    'SKILL': 'Neurotoxin'}
        self.assertEqual(expected, actual)

    def test_determine_enemy_level_two(self):
        char = make_character("Justin", 2, 0)
        actual = determine_enemy(char)
        expected = {'ATTACK': 15,
                    'EXP': 150,
                    'HP': 200,
                    'MAXIMUM_HP': 200,
                    'NAME': 'Evelynn',
                    'SKILL': 'Hate Spike'}
        self.assertEqual(expected, actual)

    def test_determine_enemy_level_three(self):
        char = make_character("Justin", 3, 0)
        actual = determine_enemy(char)
        expected = {'ATTACK': 20,
                    'EXP': 200,
                    'HP': 300,
                    'MAXIMUM_HP': 300,
                    'NAME': 'Karthus',
                    'SKILL': 'Requiem'}
        self.assertEqual(expected, actual)

    def test_determine_enemy_boss(self):
        char = make_character("Justin", 3, 0)
        char["X-coordinate"] = 4
        char["Y-coordinate"] = 4
        actual = determine_enemy(char)
        expected = {'ATTACK': 25,
                    'EXP': 500,
                    'HP': 900,
                    'MAXIMUM_HP': 900,
                    'NAME': 'Yuumi',
                    'SKILL': 'Final Chapter'}
        self.assertEqual(expected, actual)
