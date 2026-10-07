def single_LR(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)

    sum_xy = 0
    sum_x2 = 0

    for i, d in zip(x, y):
        sum_xy += i * d
        sum_x2 += i ** 2

    sum_x_2 = sum_x ** 2

    mn = (n * sum_xy) - (sum_x * sum_y)
    md = (n * sum_x2) - sum_x_2

    m = mn / md
    c = (sum_y - m * sum_x) / n

    return m, c


def main():
    height = [5.5, 5.8, 6.0, 5.0]
    weight = [60, 70, 80, 50]

    # x = weight, y = height
    m, c = single_LR(weight, height)

    while True:
        print("Enter weight for height prediction:")
        x = float(input())

        y = m * x + c

        print(f"Your predicted height is: {y:.2f} ft")
        print("-"*30)


if __name__ == "__main__":
    main()