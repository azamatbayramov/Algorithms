def sort(lst):
    start = 0

    while start < len(lst):
        min_i = start

        for i in range(start, len(lst)):
            if lst[i] < lst[min_i]:
                min_i = i

        lst[start], lst[min_i] = lst[min_i], lst[start]

        start += 1

    return lst


print(sort([1, 2, 1, 4, 3, 5, 3, 5]))  # [1, 1, 2, 3, 3, 4, 5, 5]
