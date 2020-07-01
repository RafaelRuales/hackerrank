def diagonalDifference(arr):
    a = 0
    b = 0
    b_counter = -1
    for index, element in enumerate(arr):
        a += element[index]
        b += element[b_counter]
        b_counter = b_counter - 1
    return abs(a-b)
