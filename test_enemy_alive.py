from unittest import TestCase
import game


class TestEnemyAlive(TestCase):
    def test_enemy_alive_false(self):
        char = game.make_character("Justin", 1, 0)
        enemy = game.determine_enemy(char)
        enemy['HP'] = 0
        actual = game.enemy_alive(enemy)
        expected = False
        self.assertEqual(expected, actual)

    def test_character_enemy_alive_true(self):
        char = game.make_character("Justin", 1, 0)
        enemy = game.determine_enemy(char)
        actual = game.enemy_alive(enemy)
        expected = True
        self.assertEqual(expected, actual)
