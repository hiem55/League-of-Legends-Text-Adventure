from unittest import TestCase
import game


class TestCheckAchievedGoal(TestCase):
    def test_check_achieved_goal_true(self):
        char = game.make_character("Justin", 1, 0)
        char["X-coordinate"] = 4
        char["Y-coordinate"] = 4
        actual = game.check_achieved_goal(char)
        expected = True
        self.assertEqual(expected, actual)

    def test_check_achieved_goal_false(self):
        char = game.make_character("Justin", 1, 0)
        actual = game.check_achieved_goal(char)
        expected = False
        self.assertEqual(expected, actual)
