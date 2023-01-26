def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        Left_array = array[:mid]
        Right_array = array[mid:]
        mergeSort(Left_array)
        mergeSort(Right_array)

        i = j = k = 0

array = [17,51,52,31,28,47,50,61,43,65]