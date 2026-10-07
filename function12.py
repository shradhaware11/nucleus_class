def Add(l1, l2, l3, func):
    length = len(l1)
    result = []

    for i in range(length):
        a = func(l1[i], l2[i], l3[i])
        result.append(a)

    return result


def add(a, b):
    return a + b


def add_3(a, b, c):
    return a + b + c


def main():
    result = Add([1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 2],
                 [2, 0, 8, 6, 3],
                 add_3)

    print(result)


if __name__ == "__main__":
    main()