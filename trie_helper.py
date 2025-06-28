from array import array

def leafs_count(max_values: array[int]) -> int:
    count = 1
    for m in max_values:
        count *= m
    return count
