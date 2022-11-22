def a():
    values = [i for i in range(1, 1001) if (i % 3 == 0 or i % 7 == 0 or i % 11 == 0) and i % 8 != 0]
    values.sort(reverse=True)

    for i in values:
        print(i)
