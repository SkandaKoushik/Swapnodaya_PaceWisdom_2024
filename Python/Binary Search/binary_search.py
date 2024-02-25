
def binary_search(arr, t):
    l = 0
    h = len(arr)
        
    while l <= h:
        mid = (l + h) // 2
        
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            l = mid + 1
        else:
            h = mid - 1
            
    return -1

