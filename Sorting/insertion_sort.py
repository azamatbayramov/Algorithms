def sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 1 and lst[j - 1] > x:
            lst[j] = lst[j - 1]
            j -= 1

        lst[j] = x

    return lst


print(sort([1, 2, 1, 4, 3, 5, 3, 5]))  # [1, 1, 2, 3, 3, 4, 5, 5]
