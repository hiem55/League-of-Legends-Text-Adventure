from unittest import TestCase
import game


class TestCharacterAlive(TestCase):
    def test_character_alive_true(self):
        char = game.make_character("Justin", 1, 0)
        char['Current HP'] = 50
        actual = game.character_alive(char)
        expected = True
        self.assertEqual(expected, actual)

    def test_character_alive_false(self):
        char = game.make_character("Justin", 1, 0)
        char['Current HP'] = 0
        actual = game.character_alive(char)
        expected = False
        self.assertEqual(expected, actual)
