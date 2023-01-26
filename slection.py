array ={17,51,52,31,28,47,50,61,43,65}

def selection_sort(array):
    for i in range(0, len(array)-1):
        min=i
        for j in range(i+1, len(array)):
            if array[j] < array [min]:
                min=j
        
        array[i], array[min]=array[min], array[i]

selection_sort(array)
print(array)