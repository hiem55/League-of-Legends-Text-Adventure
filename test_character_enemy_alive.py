from unittest import TestCase
import game


class TestCharacterEnemyAlive(TestCase):
    def test_character_enemy_alive(self):
        char = game.make_character("Justin", 1, 0)
        enemy = game.determine_enemy(char)
        actual = game.character_enemy_alive(char, enemy)
        expected = True
        self.assertEqual(expected, actual)

    def test_character_enemy_alive_only_character(self):
        char = game.make_character("Justin", 1, 0)
        enemy = game.determine_enemy(char)
        enemy["HP"] = 0
        actual = game.character_enemy_alive(char, enemy)
        expected = False
        self.assertEqual(expected, actual)

    def test_character_enemy_alive_only_enemy(self):
        char = game.make_character("Justin", 1, 0)
        enemy = game.determine_enemy(char)
        char["Current HP"] = 0
        actual = game.character_enemy_alive(char, enemy)
        expected = False
        self.assertEqual(expected, actual)

    def test_character_enemy_alive_both_dead(self):
        char = game.make_character("Justin", 1, 0)
        enemy = game.determine_enemy(char)
        char["Current HP"] = 0
        enemy["HP"] = 0
        actual = game.character_enemy_alive(char, enemy)
        expected = False
        self.assertEqual(expected, actual)
