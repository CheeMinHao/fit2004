def radix_sort(new_list, col):

    for i in range(col):
        # Find the Maximum
        max_item = new_list[0]
        max_item_remainder = (max_item // (10 ** i)) % 10
        for item in new_list:
            item_remainder = (item // (10 ** i)) % 10
            if item_remainder > max_item_remainder:
                max_item = item

        # Initialize the Array
        count_array = [None] * 10
        for k in range(len(count_array)):
            count_array[k] = []

        # Update Count Array
        for item in new_list:
            item_remainder = (item // (10 ** i)) % 10
            count_array[item_remainder].append(item)

        # Update Input Array
        index = 0
        for l in range(len(count_array)):
            item = l
            frequency = count_array[l]
            for j in range(len(frequency)):
                new_list[index] = frequency[j]
                index = index + 1


    return new_list