import unittest
from password_checker import check_password


class TestPasswordChecker(unittest.TestCase):

    def test_weak_password(self):
        strength, score, suggestions = check_password("hello")
        self.assertEqual(strength, "Weak")

    def test_strong_password(self):
        strength, score, suggestions = check_password(
            "BlueTiger@River92!"
        )
        self.assertEqual(strength, "Strong")
        self.assertEqual(score, 6)

    def test_common_password_pattern(self):
        strength, score, suggestions = check_password("password123!")
        self.assertEqual(strength, "Weak")
        self.assertTrue(any("common" in s.lower() for s in suggestions))

    def test_missing_special_character(self):
        strength, score, suggestions = check_password("BlueTigerRiver92")
        self.assertTrue(
            any("special character" in s.lower() for s in suggestions)
        )

    def test_short_password(self):
        strength, score, suggestions = check_password("Ab1!")
        self.assertEqual(strength, "Weak")


if __name__ == "__main__":
    unittest.main()