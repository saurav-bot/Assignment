import unittest
from credit_card_validator import validator

class TestValidator(unittest.TestCase):
    def test_validator(self):
        number = "379354508162306"
        result = validator(number)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()