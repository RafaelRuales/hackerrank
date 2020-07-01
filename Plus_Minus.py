def plusMinus(arr):
    results = {"less_than_zero": 0, "zero": 0, "more_than_zero":0}
    for num in arr:
        if num < 0:
            results["less_than_zero"] += 1
        elif num == 0:
            results["zero"] += 1
        else:
            results["more_than_zero"] += 1
                    
    more_than_zero = results["more_than_zero"] / len(arr)
    less_than_zero = results["less_than_zero"] / len(arr)
    zero = results["zero"] / len(arr)

    print("{0:.6f}".format(more_than_zero))
    print("{0:.6f}".format(less_than_zero))
    print("{0:.6f}".format(zero))

    return results
