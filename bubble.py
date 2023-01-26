def bubble_sort(array):
    num = len(array)

    for i in range(num-1):
        swap = 0
        for j in range (0, num-i-1):
            if array[j] > array[j +1]:
                array[j+1], array[j] = array[j], array[j+1]
                swap = 1
        if swap ==0:
            break
    return array

array =[17,51,52,31,28,47,50,61,43,65]
print("Array in Ascending Order using Bubble Sort")
print(bubble_sort(array))


