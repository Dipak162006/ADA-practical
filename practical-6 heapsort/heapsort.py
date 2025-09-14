def heapify(a, n, i):   
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and a[left] > a[largest]:
            largest = left
        if right < n and a[right] > a[largest]:
            largest = right

        if largest == i:
            break

        a[i], a[largest] = a[largest], a[i]
        i = largest

def heapsort(a):
    n = len(a)

    # Build max heap
    for i in reversed(range(n // 2)):
        heapify(a, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]  # swap
        heapify(a, i, 0)

# Sample usage
a = [3, 4, 7, 2, 1, 8, 9]
print("Original array:", a)
heapsort(a)
print("Sorted array:", a)
