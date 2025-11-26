import unittest
import sys 
"use sys for min and max since there is no overflow"


def can_drive(age):

   driving_age = 16

   return age >= driving_age


class TestCanDrive(unittest.TestCase):

    "Maybe they are a vampire?? haha"
    def test_max_int(self):
        self.assertTrue(can_drive(sys.maxsize))

    def test_min_int(self):
        self.assertFalse(can_drive(-sys.maxsize - 1))

    def test_exact_driving_age(self):
        "Should return true"
        self.assertTrue(can_drive(16))

    def test_above_driving_age(self):
        "Should return true"
        self.assertTrue(can_drive(17))
        self.assertTrue(can_drive(40))

    def test_below_driving_age(self):
        """Should return false"""
        self.assertFalse(can_drive(15))
        self.assertFalse(can_drive(10))

    def test_negative_age(self):
        "Should return false"
        self.assertFalse(can_drive(-1))

    def test_non_integer_input(self):
        "Error cases"
        with self.assertRaises(TypeError):
            can_drive("sixteen")
        with self.assertRaises(TypeError):
            can_drive(None)


if __name__ == "__main__":
    unittest.main()