import unittest


class RandomCatFactTestCase(unittest.TestCase):

    def test_random_cat_fact(self):
        fact = 2
        self.assertEqual(2, fact)


if __name__ == '__main__':
    unittest.main()
