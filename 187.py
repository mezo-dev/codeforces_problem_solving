





def min_value(arr: list[int]) -> int:
    min_val = arr[0]

    for i in arr:
        if i < min_val:
            min_val = i
    return min_val


print(min_value(arr=[7, 12, 9, 4, 11, 8]))