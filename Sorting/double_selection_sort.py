def sort(lst):
    start = 0
    finish = len(lst) - 1

    while start < finish:
        min_i = start
        max_i = finish

        for i in range(start, finish + 1):
            if lst[i] < lst[min_i]:
                min_i = i
            if lst[i] > lst[max_i]:
                max_i = i

        lst[start], lst[min_i], lst[finish], lst[max_i] = \
            lst[min_i], lst[start], lst[max_i], lst[finish]

        start += 1
        finish -= 1

    return lst


print(sort([1, 2, 1, 4, 3, 5, 3, 5]))  # [1, 1, 2, 3, 3, 4, 5, 5]
