''' 
Merge Sort is based on the "Divide and Conquer Algorithm". It 
divides the input array into smaller parts and merge them in Order. The Time Complexity is O(N.LOG(N)) ,it is because log(n) calls and merging takes O(N) linera time in each call.
'''

def mergeSort(arr):
  if len(arr)>1 :
    mid = len(arr)//2 
    left=arr[:mid]
    right=arr[mid:]

    mergeSort(left)
    mergeSort(right)

    i,j,k=0,0,0

    while i<len(left) and j<len(right) :
      if left[i] <= right[j] :
        arr[k] = left[i]
        i+=1
      else:
        arr[k] = right[j]
        j+=1
      k+=1

    while i<len(left) :
      arr[k]=left[i]
      i+=1
      k+=1
    
    while j<len(right):
      arr[k]=right[j]
      j+=1
      k+=1
  
  return arr


arr=[int(x) for x in input().split()]
print(mergeSort(arr))
