#! usr/bin/python3

"""Program that implements a test for selection_sort."""

import selection_sort
import unittest

class SelectionSortTest(unittest.TestCase):

  def testSelectionSortInts(self):
    list_ints = [4, 2, 1, 9, 3, 7, 5, 6]
    self.assertEqual(selection_sort.selection_sort(list_ints),
        [1, 2, 3, 4, 5, 6, 7, 9])

  def testSelectionSortStrings(self):
    list_strings = ['this', 'is', 'my', 'test', 'list']
    self.assertEqual(selection_sort.selection_sort(list_strings),
        ['is', 'list', 'my', 'test', 'this'])

if __name__ == '__main__':
  unittest.main()