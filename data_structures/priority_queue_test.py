#! /usr/bin/python3

""" This script runs unit tests on priority_queue.py."""

import priority_queue
import unittest

class QueueTest(unittest.TestCase):

  def testQueue(self):
    queue_a = priority_queue.PriorityQueue()
    queue_a.push(11)
    queue_a.push(2)
    queue_a.push(13)
    first_item_removed = queue_a.pop()
    queue_a.push(29)
    self.assertEqual(first_item_removed, 13)
    self.assertFalse(queue_a.is_empty())
    self.assertEqual(queue_a.pop(), 29)
    self.assertEqual(queue_a.pop(), 11)
    self.assertEqual(queue_a.pop(), 2)

if __name__ == '__main__':
  unittest.main()