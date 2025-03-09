import unittest

from ClassBuilder import ClassBuilder


class MyTestCase(unittest.TestCase):
    def test_constructor_assigns_name(self):
        sut = ClassBuilder("My Name")
        self.assertEqual(sut.name, "My Name")

if __name__ == '__main__':
    unittest.main()
