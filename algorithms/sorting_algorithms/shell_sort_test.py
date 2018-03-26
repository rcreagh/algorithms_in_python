#! usr/bin/python3

"""Program that implements a test for shell_sort."""

import shell_sort
import unittest

class shellSortTest(unittest.TestCase):

  def testShellSortInts(self):
    list_ints = [4, 2, 1, 9, 3, 7, 5, 6]
    self.assertEqual(shell_sort.shell_sort(list_ints),
        [1, 2, 3, 4, 5, 6, 7, 9])

  def testShellSortStrings(self):
    list_strings = ['this', 'is', 'my', 'test', 'list']
    self.assertEqual(shell_sort.shell_sort(list_strings),
        ['is', 'list', 'my', 'test', 'this'])

if __name__ == '__main__':
  unittest.main()