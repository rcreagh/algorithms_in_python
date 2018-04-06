#! usr/bin/python3

"""This program implements bottom up merge sort as outlined in Sedgewick's
'Algoritmgs'. Note that this is essentially the same as top down mergesort
but for the implementation of 'sort'. However, I have included all code in
each of their separate files for completeness."""

def mergesortbu(array):
  copy = []
  for i in range(len(array)):
    copy.append(array[i])
  print(copy)
  def merge(array, lo, mid, hi):
    print("Merging" + str(array) + " hi: " + str(hi) + " lo: " + str(lo)
        + " mid: " + str(mid))
    lo_index = lo
    hi_index = mid + 1
    for i in range(lo, hi + 1):
      copy[i] = array[i]
    for i in range(lo, hi + 1):
      # If all of the left array has already been added to the final array.
      if lo_index > mid:
        array[i] = copy[hi_index]
        hi_index += 1
      # If all of the right array has already been added to the final array.
      elif hi_index > hi:
        array[i] = copy[lo_index]
        lo_index += 1
      # If next item in left array is less than next item in right array.
      elif copy[lo_index] < copy[hi_index]:
        array[i] = copy[lo_index]
        lo_index += 1
      # If next item in right array is less than next item in left array.
      else:
        array[i] = copy[hi_index]
        hi_index += 1

  def sort(array, lo, hi):
    jump_length = 1
    n = len(array)
    while jump_length < n:
      lo = 0
      while lo < n - jump_length:
        merge(array, lo, lo + jump_length - 1, min(
            lo + jump_length + jump_length - 1, n - 1))
        lo += jump_length*2
      jump_length = jump_length*2

  sort(array, 0, len(array) - 1)
  return array