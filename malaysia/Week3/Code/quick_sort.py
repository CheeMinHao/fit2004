def quick_sort(new_list, start, end):
    """
    Sorts elements with Quick Sort
    :invariant: left <= pivot, right > pivot
    :partitioning:
    - Out-of-Place Partitioning
        > Need left and right temporary list, hence O(N) Aux Space beside recursive stack
        > Then combined back to original list
        > Not Stable, but can make it stable by having 2 separate list for == pivot (More memory)
    - Hoare's
        > 
    """
    if start < end:
        boundary = partition(new_list, start, end)
        quick_sort(new_list, start, boundary - 1)
        quick_sort(new_list, boundary + 1, end)

def partition(array, start, end):

    # Initialise Mid value of the list as pivot
    mid = (start + end) // 2
    pivot = array[mid]

    # Swap starting element with pivot (mid element)
    array[start], array[mid] = array[mid], array[start]

    # boundary = first element after pivot
    boundary = start

    # Executes sorting according to comparison with pivot
    for k in range(start + 1, end + 1):

        # Checks if current element is smaller or equals to pivot
        if array[k] <= pivot:

            # If yes, then increase boundary by 1 and swap current element with boundary value
            boundary += 1
            array[k], array[boundary] = array[boundary], array[k]
    
    # swap back the pivot into its sorted position
    array[start], array[boundary] = array[boundary], array[start]

    return boundary

if __name__ == "__main__":
    array = [2, 4, 1, 6, 5, 3, 5]
    quick_sort(array, 0, len(array) - 1)
    print(array)