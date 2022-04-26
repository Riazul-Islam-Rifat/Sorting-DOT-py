# Insertion sort
def insertion_sort(arr):
  for key in range(1,len(arr)):
    key_element=arr[key]
    j=key-1
    while j>=0 and key_element<arr[j]:
      arr[j+1]=arr[j]
      j=j-1
    arr[j+1]=key_element
  return arr
given_array=[4,1,7,9,2,6,10,77,55]
sorted_array=insertion_sort(given_array)
print('after_sorting', sorted_array)