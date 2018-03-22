#! usr/bin/python3

import union_find
import unittest

class UnionFindTest(unittest.TestCase):

  def testUnionFind(self):
    list_of_tuples = [[0, 3], [0, 1], [2, 4], [4, 5], [1, 6], [1, 7], [5, 8]]
    number_of_nodes = 10
    self.assertEqual(union_find.union_find(number_of_nodes, list_of_tuples), 3)

if __name__ == '__main__':
  unittest.main()