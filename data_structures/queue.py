#! /usr/bin/python3

"""This script implements a queue based on a linked list, as per Sedgewick's
'Algorithms'."""

class DequeueEmptyQueue(Exception):
  pass

class Queue:

  class Node:
    def __init__(self, item, next):
      self.item = item
      self.next = next

  def __init__(self):
    self.n = 0
    self.first = None
    self.last = None

  def is_empty(self):
    return self.n == 0

  def size(self):
    return self.n

  def enqueue(self, item):
    old_last = self.last
    self.last = Queue.Node(item, None)
    if self.is_empty():
      self.first = self.last
    else:
      old_last.next = self.last
    self.n += 1

  def dequeue(self):
    if self.n == 0:
      raise DequeueEmptyQueue("ERROR: Cannot dequeue from an empty queue.")
    item = self.first.item
    self.first = self.first.next
    self.n -= 1
    if self.is_empty():
      self.last = None
    return item