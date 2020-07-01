def miniMaxSum(arr):
    arr.sort()
    max_result = 0
    min_result = 0
    for num in arr[1:]:
        max_result += num
    for num in arr[:4]:
        min_result += num
    return min_result, max_result
