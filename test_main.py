# ref : https://docs.python.org/3/library/unittest.html#assert-methods

import unittest
import main as m


class MyTestCase(unittest.TestCase):

    def test_same(self):
        bull, cow = m.play(target_word="play", user_word="play")
        self.assertEqual(bull, 4)
        self.assertEqual(cow, 0)

    def test_no_match(self):
        bull, cow = m.play(target_word="play", user_word="risk")
        self.assertEqual(bull, 0)
        self.assertEqual(cow, 0)

    def test_1bull1(self):
        bull, cow = m.play(target_word="play", user_word="aaaa")
        self.assertEqual(bull, 1)
        self.assertEqual(cow, 0)

    def test_1bull2(self):
        bull, cow = m.play(target_word="play", user_word="aaab")
        self.assertEqual(bull, 1)
        self.assertEqual(cow, 0)

    def test_1bull3(self):
        bull, cow = m.play(target_word="play", user_word="pppp")
        self.assertEqual(bull, 1)
        self.assertEqual(cow, 0)

    def test_1bull4(self):
        bull, cow = m.play(target_word="play", user_word="ppqq")
        self.assertEqual(bull, 1)
        self.assertEqual(cow, 0)

    def test_1cow(self):
        bull, cow = m.play(target_word="play", user_word="rain")
        self.assertEqual(bull, 0)
        self.assertEqual(cow, 1)

    def test_3cow(self):
        bull, cow = m.play(target_word="play", user_word="lays")
        self.assertEqual(bull, 0)
        self.assertEqual(cow, 3)

    def test_3bull(self):
        bull, cow = m.play(target_word="coin", user_word="coil")
        self.assertEqual(bull, 3)
        self.assertEqual(cow, 0)

    def test_2cow(self):
        bull, cow = m.play(target_word="move", user_word="team")
        self.assertEqual(bull, 0)
        self.assertEqual(cow, 2)

if __name__ == '__main__':
    unittest.main()
