def pivot_partition(arr,low,high):
  pivot=arr[high]
  i=low # index pointer which indicates the swapping index for the element smaller or equal to pivot.
  j=high # index of pivot element
  for item in range(low,high):
    if arr[item]<=pivot:
      #i=i+1
      (arr[i],arr[item])=(arr[item],arr[i]) # Swapping
      i=i+1
  (arr[i],arr[j])=(arr[j],arr[i]) # Swapping with pivot element
  return i

def quickSort(arr,l,h):
  if l<h:
    partition=pivot_partition(arr,l,h)
    quickSort(arr,l,partition-1)
    quickSort(arr,partition+1,h)

given_array=[9,1,8,5,3,7,2,6,4,5]
high=len(given_array)-1
low=0
quickSort(given_array,low,high)
print('After sorting', given_array)
