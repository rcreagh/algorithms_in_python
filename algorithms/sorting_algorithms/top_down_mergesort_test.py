#! usr/bin/python3

"""Program that implements a test for top_down_mergesort."""

import top_down_mergesort
import unittest

class topDownMergeSortTest(unittest.TestCase):

  def testTdMergeSortInts(self):
    list_ints = [4, 2, 1, 9, 3, 7, 5, 6]
    self.assertEqual(top_down_mergesort.tdmergesort(list_ints),
        [1, 2, 3, 4, 5, 6, 7, 9])

  def testTdMergeSortStrings(self):
    list_strings = ['this', 'is', 'my', 'test', 'list']
    self.assertEqual(top_down_mergesort.tdmergesort(list_strings),
        ['is', 'list', 'my', 'test', 'this'])

if __name__ == '__main__':
  unittest.main()