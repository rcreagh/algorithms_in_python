#! urs/bin/python3

"""This program implements a simple way of swapping 2 items in a list. It is
possibly overkill, but anyway."""

def swap(array, index_1, index_2):
  """Function that takes a list and 2 indices to be swapped."""
  item_1 = array[index_1]
  item_2 = array[index_2]
  array[index_1] = item_2
  array[index_2] = item_1