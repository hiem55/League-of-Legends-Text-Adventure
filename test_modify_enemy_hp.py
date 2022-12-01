from unittest import TestCase
import game


class TestModifyEnemyHp(TestCase):
    def test_modify_enemy_hp(self):
        char = game.make_character("Justin", 1, 0)
        minion = game.determine_enemy(char)
        actual = game.modify_enemy_hp(char, minion)
        expected = {'ATTACK': 10,
                    'EXP': 100,
                    'HP': 52.0,
                    'MAXIMUM_HP': 100,
                    'NAME': 'Elise',
                    'SKILL': 'Neurotoxin'}
        self.assertEqual(expected, actual)
