#! /usr/bin/python3

""" This script runs unit tests on stack.py."""

import queue
import unittest

class QueueTest(unittest.TestCase):

  def testEmptyQueue(self):
    queue_a = queue.Queue()
    self.assertTrue(queue_a.is_empty())
    self.assertRaises(queue.DequeueEmptyQueue, queue_a.dequeue)

  def testQueue(self):
    queue_a = queue.Queue()
    queue_a.enqueue(1)
    queue_a.enqueue(2)
    queue_a.enqueue(3)
    item_removed = queue_a.dequeue()
    queue_a.enqueue(4)
    self.assertEqual(item_removed, 1)
    self.assertEqual(queue_a.size(), 3)
    self.assertFalse(queue_a.is_empty())
    self.assertEqual(queue_a.first.item, 2)
    self.assertEqual(queue_a.first.next.item, 3)
    self.assertEqual(queue_a.last.item, 4)
    self.assertEqual(queue_a.last.next, None)

if __name__ == '__main__':
  unittest.main()