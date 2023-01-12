import unittest
from project import show_aggie_pride


class ProjectTestCase(unittest.TestCase):
    def test_show_aggie_pride(self):
        self.assertEqual('Aggie Pride - Worldwide', show_aggie_pride())


if __name__ == '__main__':
    unittest.main()
