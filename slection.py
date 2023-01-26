

def selection_sort(array):

    for i in range(5):
        min=i
        for j in range(i, 10):
            if array[j] < array [min]:
                min=j
        
        temp = array[i]
        array[i] = array[min]
        array[min] = temp

array ={17,51,52,31,28,47,50,61,43,65}
selection_sort(array)
print(array)