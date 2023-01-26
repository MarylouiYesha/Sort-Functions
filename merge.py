def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        Left_array = array[:mid]
        Right_array = array[mid:]
        mergeSort(Left_array)
        mergeSort(Right_array)

        i = j = k = 0

        while i < len(Left_array) and j < len(Right_array):
            if Left_array[i] <= Right_array[j]:
                array[k] = Left_array[i]
                i += 1
            else:
                array[k] = Right_array[j]
                j += 1
            k += 1

        while i < len(Left_array):
            array[k] = Left_array[i]
            i += 1
            k += 1

        while j < len(Right_array):
            array[k] = Right_array[j]
            j += 1
            k += 1

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__ == '__main__':
    print("Array in Ascending Order using Merge Sort")
    array = [17,51,52,31,28,47,50,61,43,65]
    mergeSort(array)
    printList(array)