cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def sum(list):
    for x in list:
        if int(x) - 10 == 0:
            list[x] = 3
    return list


print(sum(cards))