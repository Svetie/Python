# selection sort algorithm
arr = [3,7,22,1,9,6,4]
def selection_sort(arr):
    for i in range(len(arr)):
    # first element is minimum value
        min = i
        # start with second element
        for j in range(i+1, len(arr)):
            if (arr[min] > arr[j]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selection_sort(arr))