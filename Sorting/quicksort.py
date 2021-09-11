def sort(lst):
    if len(lst) < 2:
        return lst
    else:
        lst_l, lst_r = list(), list()

        mid = len(lst) // 2
        p = lst[mid]

        for i in lst[:mid] + lst[mid + 1:]:
            if i < p:
                lst_l.append(i)
            else:
                lst_r.append(i)

        return sort(lst_l) + [p] + sort(lst_r)


print(sort([1, 2, 1, 4, 3, 5, 3, 5]))  # [1, 1, 2, 3, 3, 4, 5, 5]
