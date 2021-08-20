def sort(lst):
    l, r = 0, len(lst) - 1

    list_sorted = False

    while not list_sorted:
        list_sorted = True

        for i in range(l, r - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                list_sorted = False
        r -= 1

        if list_sorted:
            break

        for i in range(r, l + 1, -1):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                list_sorted = False
        l += 1

    return lst


print(sort([1, 2, 1, 4, 3, 5, 3, 5]))  # [1, 1, 2, 3, 3, 4, 5, 5]
