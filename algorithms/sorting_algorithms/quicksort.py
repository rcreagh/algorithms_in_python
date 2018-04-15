#! usr/bin/python3

"""This program implements quicksort as outlined in Sedgewick's 'Algorithms'."""

import random

def quicksort(array):
  def partition(array, lo, hi):
    partition_value = array[lo]
    scan_right = lo + 1
    scan_left = hi
    while True:
      # Scan right until a value greater than the parition item is found.
      while array[scan_right] < partition_value:
        if scan_right == hi:
          break
        scan_right += 1
      # Scan left until a value less than the parition item is found.
      while array[scan_left] > partition_value:
        if scan_left == lo:
          break
        scan_left -= 1
      if scan_right >= scan_left:
        break
      # Swap values on wrong side of partition.
      array[scan_left], array[scan_right] = array[scan_right], array[scan_left]
    # Put the exchange value (array[lo]) into the correct place.
    array[lo], array[scan_left] = array[scan_left], array[lo]

    return scan_left

  def sort(array, lo, hi):
    if hi <= lo:
      return
    partition_item = partition(array, lo, hi)
    # Partition item is now in the right place, so only need to sort items to
    # either side of it.
    sort(array, lo, partition_item - 1)
    sort(array, partition_item + 1, hi)

  random.shuffle(array)
  sort(array, 0, len(array) - 1)
  return array