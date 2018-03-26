#! usr/bin/python3

"""This program implements 'Selection Sort" as outlined in Sedgewick's
'Algorithms'. Note, this is for learning purposes only. Selection sort's
quadratic run time is not useful in practice. There are of course far more
efficient ways to sort a list of items."""

import swap

def selection_sort(array):
  """Function that takes a list and returns it sorted."""
  for i in range(len(array)):
    min_index = i
    min_val = array[i]
    for j in range(i + 1, len(array)):
      if array[j] < min_val:
        min_val = array[j]
        min_index = j
    swap.swap(array, i, min_index)
  print(array)
  return array