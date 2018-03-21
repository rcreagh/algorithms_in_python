#! /usr/bin/python3

""" This script runs unit tests on stack.py."""

import stack
import unittest

class StackTest(unittest.TestCase):

  def testEmptyStack(self):
    """Tests that isEmpty() returns True when stack is empty, and that you
    cannot pop() from an empty stack."""
    stack_a = stack.Stack()
    self.assertTrue(stack_a.isEmpty())
    self.assertRaises(stack.PopFromEmptyStackException, stack_a.pop)

  def testStack(self):
    stack_a = stack.Stack()
    stack_a.push(1)
    stack_a.push(2)
    stack_a.push(3)
    item_removed = stack_a.pop()
    stack_a.push(4)
    print(stack_a)
    self.assertEqual(item_removed, 3)
    self.assertEqual(stack_a.stack, [1, 2, 4])

if __name__ == '__main__':
  unittest.main()