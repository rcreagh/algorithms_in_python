 #! usr/bin/python3

"""Program that implements a test for quicksort."""

import quicksort
import unittest

class quickSortTest(unittest.TestCase):

  def testQuickSortInts(self):
    list_ints = [4, 2, 1, 9, 3, 7, 5, 6]
    self.assertEqual(quicksort.quicksort(list_ints),
        [1, 2, 3, 4, 5, 6, 7, 9])

  def testQuickSortStrings(self):
    list_strings = ['this', 'is', 'my', 'test', 'list']
    self.assertEqual(quicksort.quicksort(list_strings),
        ['is', 'list', 'my', 'test', 'this'])

if __name__ == '__main__':
  unittest.main()