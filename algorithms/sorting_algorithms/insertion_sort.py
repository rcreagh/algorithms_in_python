#! usr/bin/python3

"""This program implements 'Selection Sort" as outlined in Sedgewick's
'Algorithms'. Note, this is for learning purposes only. Selection sort's
quadratic run time is not useful in practice if implemented on its own. There
are of course far more efficient ways to sort a list of items."""

import swap

def insertion_sort(array):
  for i in range(1, len(array)):
    j = i
    while j > 0 and array[j] < array[j - 1]:
      swap.swap(array, j, j - 1)
      j -= 1
  print(array)
  return array