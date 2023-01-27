def quick_sort (array, left, right):
    if left < right:
        part=part(array, left, right)
        quick_sort(array, left, part - 1)
        quick_sort(array, part + 1, right)

def part(array, left, right):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j:
        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] >= pivot:
            j -= 1
        if i < j:
            array[1], array[j] = array[j], array[i]


array = [17,51,52,31,28,47,50,61,43,65]