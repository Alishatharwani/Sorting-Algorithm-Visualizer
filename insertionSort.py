import time

def insertion_sort(data, drawData, timeTick):
    # Traverse through 1 to len(data)
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >=0 and key < data[j] :
                data[j+1] = data[j]
                j -= 1
                drawData(data, ['yellow' if x == j else 'green' if x == i else 'red' for x in range(len(data))])
                time.sleep(timeTick)
        data[j+1] = key
    
    drawData(data, ['green' for x in range(len(data))])
