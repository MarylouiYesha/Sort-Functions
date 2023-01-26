def selection_sort(array,size):

    for i in range(size):
        min=i

        for j in range(i + 1, size):
            if array[j] < array[min]:
                min=j
        
        (array[i], array[min]) = (array[min], array[i])

print("Array in Ascending Order using Selection sort")
array =[17,51,52,31,28,47,50,61,43,65]
size = len(array)
selection_sort(array,size)
print(array)