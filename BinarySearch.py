def binary_search(arr, target):
 low, high = 0, len(arr) - 1
 while low <= high:
  mid = (low + high) // 2
  
  # Check if the target is present at the middle
  if arr[mid] == target:
   return mid
  
  # If the target is smaller, ignore the right half
  elif arr[mid] > target:
   high = mid - 1
  
  # If the target is larger, ignore the left half
  else:
   low = mid + 1
 return -1 # Return -1 if the target is not found

# Example usage:
7
arr = [27, 34, 88, 1, 99, 77, 9, 8, 47, 66]
target = 27
print("array:", arr)
print("Target:", target)

# Perform binary search
result = binary_search(arr, target)
if result != -1:
 print(f"Target found at index {result}.")
else:
 print("Target not found in the array.")