def linear_search(target_list, target_item):
    for index in range(len(target_list)):
        if target_list[index] == target_item:
            return index
    return -1


def binary_search(target_list, target_item):
    start_index = 0
    final_index = len(target_list) - 1
    while start_index <= final_index:
        middle_index = (start_index + final_index) // 2
        if target_list[middle_index] < target_item:
            start_index = middle_index + 1
        elif target_list[middle_index] > target_item:
            final_index = middle_index - 1
        else:
            return middle_index
    return -1


def doubling_search(target_list, target_item):
    length = len(target_list)
    if target_list[0] == target_item:
        return 0
    index = 1
    while index < length and target_list[index] <= target_item:
        index *= 2
    result = binary_search(target_list[int(index / 2):(min(index, length))], target_item)
    if result == -1:
        return -1
    else:
        return int(result + index / 2)