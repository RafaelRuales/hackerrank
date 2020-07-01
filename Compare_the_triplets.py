def compareTriplets(a, b):
    score = {"a": 0, "b": 0}
    for value in range(3):
        if a[value] > b[value]:
            score["a"] += 1
        elif a[value] < b[value]:
            score["b"] += 1
    result = [score["a"],score["b"]]
    return result
