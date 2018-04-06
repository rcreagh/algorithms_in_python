 #! usr/bin/python3

"""Program that implements a test for bottom_up_mergesort."""

import bottom_up_mergesort
import unittest

class bottomUpMergeSortTest(unittest.TestCase):

  def testMergeSortBUInts(self):
    list_ints = [4, 2, 1, 9, 3, 7, 5, 6]
    self.assertEqual(bottom_up_mergesort.mergesortbu(list_ints),
        [1, 2, 3, 4, 5, 6, 7, 9])

  def testMergeBUSortStrings(self):
    list_strings = ['this', 'is', 'my', 'test', 'list']
    self.assertEqual(bottom_up_mergesort.mergesortbu(list_strings),
        ['is', 'list', 'my', 'test', 'this'])

if __name__ == '__main__':
  unittest.main()