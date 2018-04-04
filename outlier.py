def find_outlier(integers):
    even = []
    odd = []

    for i in integers:
        if (i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 1:
        return even[0]
    else:
        return odd[0]

    return None

integers = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(integers))
