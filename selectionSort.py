import time

def selection_sort(data, drawData, timeTick):
    # Traverse through all array elements
    for i in range(len(data)):
      
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
            drawData(data, ['yellow' if x == j or x == min_idx else 'red' for x in range(len(data))])
            time.sleep(timeTick)
                      
        # Swap the found minimum element with the first element        
        data[i], data[min_idx] = data[min_idx], data[i]

    drawData(data, ['green' for x in range(len(data))])
