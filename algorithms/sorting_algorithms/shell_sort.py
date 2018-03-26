#! usr/bin/python3

"""THis program implements 'Shell Sort' as outlined in Sedgewick's
'Algoritms'."""

import swap

def shell_sort(array):
  h = 1
  # Define value for h, for h-sorting the list.
  while h < len(array)//3:
    h = h*3 + 1
  while h >= 1:
    i = h
    while i < len(array):
      j = i
      while j >= h and array[j] < array[j - h]:
        swap.swap(array, j, j - h)
        j -= h
      i += h
    h = h//3
  print(array)
  return array