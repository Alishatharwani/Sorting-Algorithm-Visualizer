import time

def heapify(data, n, i, drawData, timeTick):
    """
    To heapify subtree rooted at index i.
    n is size of heap.
    """
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and data[i] < data[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and data[largest] < data[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        data[i], data[largest] = data[largest], data[i]  # swap
        drawData(data, ['green' if x == i or x == largest else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        # Heapify the root.
        heapify(data, n, largest, drawData, timeTick)

def heap_sort(data, drawData, timeTick):
    """The main function to sort an array of given size"""
    n = len(data)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(data, n, i, drawData, timeTick)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]   # swap
        drawData(data, ['green' if x == i or x == 0 else 'red' for x in range(len(data))])
        time.sleep(timeTick)
        heapify(data, i, 0, drawData, timeTick)
    
    drawData(data, ['green' for x in range(len(data))])

