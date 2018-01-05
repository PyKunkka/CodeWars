def multiple_of_index(arr):
    result = []
    i = 1
    while i < len(arr):
        if arr[i] % i == 0:
            result.append(arr[i])
        i += 1
    return result