#! usr/bin/python3

def tdmergesort(array):
  copy = []
  for i in range(len(array)):
    copy.append(array[i])
  print(copy)
  def merge(array, hi, lo, mid):
    print("Merging" + str(array) + " hi: " + str(hi) + " lo: " + str(lo)
        + " mid: " + str(mid))
    """Function that merges two sorted arrays into a single sorted array."""
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
    if hi <= lo:
      return
    mid = lo + (hi - lo)//2
    sort(array, lo, mid)
    sort(array, mid + 1, hi)
    merge(array, hi, lo, mid)

  sort(array, 0, len(array) - 1)
  return array