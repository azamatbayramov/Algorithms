def sort(lst):
    lst_sorted = False
    while not lst_sorted:
        lst_sorted = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                lst_sorted = False
    return lst


print(sort([1, 2, 1, 4, 3, 5, 3, 5]))  # [1, 1, 2, 3, 3, 4, 5, 5]
