def quick_sort_dnf(new_list, start, end):
    if start < end:
        boundary1, boundary2 = dutch_national_flag(new_list, start, end)
        quick_sort_dnf(new_list, start, boundary1)
        quick_sort_dnf(new_list, boundary2, end)

def dutch_national_flag(new_list, start, end):

    mid = (start + end) // 2
    pivot = array[mid]
    
    place = start
    while place <= end:
        if array[place] < pivot:
            array[place], array[start] = array[start], array[place]
            start += 1
            place += 1
        elif array[place] == pivot:
            mid += 1
        else:
            array[place], array[end] = array[end], array[place]

    return start, place
    
    
    


if __name__ == "__main__":
    array = [2, 4, 1, 6, 5, 3, 5]
    quick_sort_dnf(array, 0, len(array) - 1)
    print(array)