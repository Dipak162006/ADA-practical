def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        lh = arr[:mid]
        rh= arr[mid:]

       
        merge_sort(lh)
        merge_sort(rh)

        
        i = j = k = 0

       
        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                arr[k] = lh[i]
                i += 1
            else:
                arr[k] = rh[j]
                j += 1
            k += 1

        # Check for any remaining elements
        while i < len(lh):
            arr[k] = lh[i]
            i += 1
            k += 1

        while j < len(rh):
            arr[k] = rh[j]
            j += 1
            k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
