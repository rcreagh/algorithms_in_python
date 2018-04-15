#! usr/bin/python3

""" This programe implements a priority queue as outlined in Sedgewick's
'Algorithms'."""

class PriorityQueue:
  def __init__(self):
    self.n = 0
    self.pq = [None] # pq[0] is unused.

  def is_empty(self):
    return self.n == 0

  def sift_up(self, key):
    while key > 1 and self.pq[key] > self.pq[key//2]:
      self.pq[key], self.pq[key//2] = self.pq[key//2], self.pq[key]
      key = key//2

  def sift_down(self, key):
    while 2*key <= self.n:
      left_child = key*2
      right_child = key*2 + 1

      # Determine larger value of left and right children
      if left_child < self.n and self.pq[right_child] < self.pq[left_child]:
        larger_child = right_child
      else:
        larger_child = left_child

      # Swap key and larger child if key is smaller than larger child.
      if self.pq[key] < self.pq[larger_child]:
        self.pq[key], self.pq[larger_child] = self.pq[larger_child], self.pq[key]
        key = larger_child
      else:
        break

  def push(self, item):
    self.n += 1
    self.pq.append(item)
    self.sift_up(self.n)

  def pop(self):
    popped_item = self.pq[1]
    self.pq[1] = self.pq[self.n]
    del self.pq[self.n]
    self.n -= 1
    if not self.is_empty():
      self.sift_down(1)
    return popped_item