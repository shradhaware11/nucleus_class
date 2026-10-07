def add(a: int, b: int, *c):
    print("a =", a)
    print("b =", b)
    print("c =", c)

    # Addition
    sum1 = 0
    for i in c:
        sum1 += i
    print("Addition =", sum1)

    # Subtraction
    sub = 0
    for i in c:
        sub -= i
    print("Subtraction =", sub)

    # Multiplication
    mul = 1
    for i in c:
        mul *= i
    print("Multiplication =", mul)


def main():
    add(10, 11, 21, 31, 33)


if __name__ == "__main__":
    main()