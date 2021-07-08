# insertion sort
arr = [1,7,4,88,3,5,89]
def insertion_sort(arr):
    # start at second element
    for i in range(1, len(arr)):
        #number to compare
        num = arr[i]
        # position of element
        position = i
        # while there is larger element
        while(position > 0 and arr[position- 1] > num):
            arr[position] = arr[position -1]
            position = position - 1
        arr[position] = num
    return arr

print(insertion_sort(arr))