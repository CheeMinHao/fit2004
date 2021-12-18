def quick_sort_hoares(new_list, start, end):
    if start < end:
        boundary = hoares(new_list, start, end)
        quick_sort(new_list, start, boundary - 1)
        quick_sort(new_list, boundary + 1, end)

def hoares(array, start, end):
    
    # Initialise Mid value of the list as pivot
    mid = (start + end) // 2
    pivot = array[mid]

    # Swap starting element with pivot (mid element)
    array[start], array[mid] = array[mid], array[start]

    boundary = start
    l_bad = start + 1
    r_bad = end

    while l_bad <= r_bad:
        while l_bad <= r_bad and array[l_bad] <= pivot:
            l_bad += 1
        while l_bad <= r_bad and array[r_bad] > pivot:
            r_bad -= 1
        if l_bad <= r_bad:
            array[l_bad], array[r_bad] = array[r_bad], array[l_bad]

    
    array[boundary], array[r_bad] = array[r_bad], array[boundary]

    boundary = r_bad

    return boundary
    


if __name__ == "__main__":
    array = [2, 4, 1, 6, 5, 3, 5]
    quick_sort(array, 0, len(array) - 1)
    print(array)