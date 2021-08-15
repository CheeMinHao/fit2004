from timeit import default_timer

def sort_counting(new_list):
    """
    Implements Basic Counting Sort on a list
    :time-complexity: O(N + M) where N is len(new_list) and M is max(new_list)
    :space-complexity: Total O(N + M) and Auxiliary O(M)
    """

    # Start Timer
    start = default_timer()

    # Find the Maximum -> O(N) where N == len(new_list)
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item

    # Initialize the Array -> O(M) where M == max(new_list)
    count_array = [0] * (max_item + 1)

    # Update Count Array -> O(N) where N == len(new_list)
    for item in new_list:
        count_array[item] += 1

    # Update Input Array -> O(M + N)
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            new_list[index] = item
            index = index + 1

    # End Timer
    end = default_timer()

    # Return sorted list along with time taken to sort the list
    return new_list, (end - start)

def sort_counting_alphabet(new_list):

    # Find the Maximum
    max_item = ord(new_list[0])
    for item in new_list:
        item = ord(item)
        if item > max_item:
            max_item = item

    # Initialize the Array
    count_array = [0] * (max_item + 1)

    # Update Count Array
    for item in new_list:
        item = ord(item)
        count_array[item] += 1

    # Update Input Array
    index = 0
    for i in range(len(count_array)):
        item = chr(i)
        frequency = count_array[i]
        for j in range(frequency):
            new_list[index] = item
            index = index + 1

    return new_list

def sort_counting_stable(new_list):

    # Find the Maximum
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item

    # Initialize the Array
    count_array = [None] * (max_item + 1)
    for i in range(len(count_array)):
        count_array[i] = []

    # Update Count Array
    for item in new_list:
        count_array[item].append(item)

    # Update Input Array
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(len(frequency)):
            new_list[index] = item
            index = index + 1

    return new_list




if __name__ == "__main__":
    import random

    small_list = []
    for i in range(10):
        small_list.append(random.randint(100, 999))

    result, time = sort_counting(small_list)
    print("Resulted List -> " + str(result))
    print("Processing Time -> " + str(time))

    large_list = []
    for i in range(10):
        large_list.append(random.randint(1000000, 9999999))

    result, time = sort_counting(large_list)
    print("Resulted List -> " + str(result))
    print("Processing Time -> " + str(time))