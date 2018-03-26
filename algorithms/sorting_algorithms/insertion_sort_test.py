#! usr/bin/python3

"""Program that implements a test for insertion_sort."""

import insertion_sort
import unittest

class InsertionSortTest(unittest.TestCase):

  def testInsertionSortInts(self):
    list_ints = [4, 2, 1, 9, 3, 7, 5, 6]
    self.assertEqual(insertion_sort.insertion_sort(list_ints),
        [1, 2, 3, 4, 5, 6, 7, 9])

  def testInsertionSortStrings(self):
    list_strings = ['this', 'is', 'my', 'test', 'list']
    self.assertEqual(insertion_sort.insertion_sort(list_strings),
        ['is', 'list', 'my', 'test', 'this'])

if __name__ == '__main__':
  unittest.main()