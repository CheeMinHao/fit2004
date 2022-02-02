def quick_sort_dnf(new_list, start, end):
    if start < end:
        boundary1, boundary2 = dutch_national_flag(new_list, start, end)
        quick_sort_dnf(new_list, start, boundary1)
        quick_sort_dnf(new_list, boundary2, end)

def dutch_national_flag(new_list, start, end):

    low = 0
    mid = 0
    pivot = new_list[(start + end) // 2]

    while mid <= end:
        if new_list[mid] < pivot: 
            new_list[mid] , new_list[low] = new_list[low], new_list[mid]
            low += 1
            mid += 1
        elif new_list[mid] == pivot:
            mid += 1
        else:
            new_list[mid] , new_list[end] = new_list[end], new_list[mid]
            end -= 1

    return low, mid
    
    


if __name__ == "__main__":
    array = [2, 4, 1, 6, 5, 3, 5]
    quick_sort_dnf(array, 0, len(array) - 1)
    print(array)