def quick_sort (array, left, right):
    if left < right:
        part=part(array, left, right)
        quick_sort(array, left, part - 1)
        quick_sort(array, part + 1, right)



array = [17,51,52,31,28,47,50,61,43,65]