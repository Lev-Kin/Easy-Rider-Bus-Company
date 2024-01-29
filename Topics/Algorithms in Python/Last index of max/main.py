def last_indexof_max(numbers):
    max_element = numbers[0]
    max_index = 0
    for index in range(1, len(numbers)):
        if numbers[index] >= max_element:
            max_element = numbers[index]
            max_index = index
    return max_index