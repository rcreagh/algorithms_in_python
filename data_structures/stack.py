#! /usr/bin/python3

""" This script implements a Pushdown Stack as outlined in Sedgewick's
'Algorithms'."""

class PopFromEmptyStackException(Exception):
  pass

class Stack:
  def __init__(self):
    self.stack = []
    self.n = 0

  def __iter__(self):
    return (item for item in self.stack)

  def __str__(self):
    return str(list(self.__iter__()))

  def is_empty(self):
    return self.n == 0

  def size(self):
    return self.n

  def push(self, item):
    """Add a new item to the stack."""
    self.stack.append(item)
    self.n += 1

  def pop(self):
    """Pop an item off of the stack."""
    if self.n == 0:
      raise PopFromEmptyStackException(
          "ERROR: Cannot pop from an empty stack.")
    self.n -= 1
    item = self.stack[self.n]
    del self.stack[self.n]
    return item