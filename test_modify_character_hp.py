from unittest import TestCase
import game


class TestModifyCharacterHp(TestCase):
    def test_modify_character_hp(self):
        char = game.make_character("Justin", 1, 0)
        minion = game.determine_enemy(char)
        actual = game.modify_character_hp(char, minion)
        expected = {'Attack': 60,
                    'Class': "Kog'maw",
                    'Current EXP': 0,
                    'Current HP': 56.0,
                    'Job': 'Ranger',
                    'Level': 1,
                    'Maximum EXP': 100,
                    'Maximum HP': 65,
                    'Name': 'Justin',
                    'Skill': 'Caustic Spittle',
                    'X-coordinate': 0,
                    'Y-coordinate': 0}
        self.assertEqual(expected, actual)
