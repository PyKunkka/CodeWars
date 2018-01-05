def iq_test(numbers):
    current_list_of_numbers = numbers.split()
    result1 = 0
    result2 = 0
    count_of_even = 0
    count_of_odd = 0
    for i in current_list_of_numbers:
        if int(i) % 2 == 0:
            result1 = i
            count_of_even += 1
        else:
            result2 = i
            count_of_odd += 1
    if count_of_even < count_of_odd:
        return (current_list_of_numbers.index(result1) + 1)
    else:
        return (current_list_of_numbers.index(result2) + 1)
