"""Unit-test cases for class project"""
import unittest
from project import show_aggie_pride


class ProjectTestCase(unittest.TestCase):
    """Unit Tests"""
    def test_show_aggie_pride(self):
        """Tests to make sure show_aggie_pride() returns the correct value"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())


if __name__ == '__main__':
    unittest.main()
