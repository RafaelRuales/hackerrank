def staircase(n):
    space = n - 1

    for i in range(1, n+1):
        print(" " * space + "#" * i)
        space -= 1
