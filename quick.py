def quick_sort (sequence):
    length = len (sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = []



print("Array in Ascending Order using Quick Sort")
[17,51,52,31,28,47,50,61,43,65]