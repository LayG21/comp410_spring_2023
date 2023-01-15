"""Unit-test cases for class project"""
import unittest
from project import show_aggie_pride, reverse_list


class ProjectTestCase(unittest.TestCase):
    """Unit Tests"""
    def test_show_aggie_pride(self):
        """Tests to make sure show_aggie_pride() returns the correct value"""
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())

    def test_reverse_list(self):
        """Test to make sure reverse_list works as expected"""
        # make sure an empty list works
        self.assertFalse(reverse_list([]))

        # try numbers
        reverse = [5, 4, 3, 2, 1]
        self.assertListEqual(reverse, reverse_list([1, 2, 3, 4, 5]))

        # try letters
        reverse = ['e', 'd', 'c', 'b', 'a']
        self.assertListEqual(reverse, reverse_list(['a', 'b', 'c', 'd', 'e']))


if __name__ == '__main__':
    unittest.main()
