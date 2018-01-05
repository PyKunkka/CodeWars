def find_outlier(integers):
    result1 = 0
    result2 = 0
    j = 0
    k = 0
    for i in integers:
        if i % 2 == 0:
             result1 = i
             j += 1       
        else:
             result2 = i
             k += 1
    if j < k:
        return result1
    else: 
        return result2
