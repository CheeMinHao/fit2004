def sort_counting(new_list):

    # Find the Maximum
    max_item = new_list[0]
    for item in new_list:
        if item > max_item:
            max_item = item

    # Initialize the Array
    count_array = [0] * (max_item + 1)

    # Update Count Array
    for item in new_list:
        count_array[item] += 1

    # Update Input Array
    index = 0
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            new_list[index] = item
            index = index + 1

    return new_list

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




