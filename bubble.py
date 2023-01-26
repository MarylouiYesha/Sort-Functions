def bubble_sort(array):
    num = len (array)
    swapped = False

    for i in range(num-1):
        for j in range (0, num-i-1):
            if array[j] > array[j +1]:
                swapped = True


array =[17,51,52,31,28,47,50,61,43,65]