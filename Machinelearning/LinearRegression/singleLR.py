import random


def data_shuffling(x, y):
    shuffle_x = []
    shuffle_y = []

    while len(x) != 0:
        index = random.randint(0, len(x) - 1)
        shuffle_x.append(x[index])
        shuffle_y.append(y[index])
        x.pop(index)
        y.pop(index)

    return shuffle_x, shuffle_y


def train_test_split(x, y, training_ratio):
    one_percent = (len(x) / 100)
    no_of_percentage = int(one_percent * training_ratio)
    
    x_train = []
    x_test = []
    y_train = []
    y_test = []

    for test in range(no_of_percentage, len(x)):
        x_test.append(x[test])
        y_test.append(y[test])

    for train in range(0, no_of_percentage):
        x_train.append(x[train])
        y_train.append(y[train])

    return x_train, x_test, y_train, y_test


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


def testing(xt, yt, m, c):
    error = 0

    for x in range(0, len(xt)):
        y = (m * xt[x]) + c
        error += yt[x] - y

    mean_error = error / len(xt)

    return mean_error


def main():

    height = [
        5.5, 5.8, 6.0, 5.0, 5.7, 6.1, 5.3, 5.9, 5.4, 6.2,
        5.6, 5.1, 5.8, 6.0, 5.5, 6.3, 5.2, 5.7, 5.9, 6.1,
        5.4, 5.6, 5.0, 5.8, 6.2, 5.3, 5.7, 6.0, 5.5, 6.1,
        5.2, 5.9, 5.6, 6.3, 5.4, 5.8, 5.1, 6.0, 5.7, 6.2,
        5.5, 5.3, 5.9, 6.1, 5.6, 5.0, 5.8, 6.2, 5.4, 5.7,
        6.0, 5.5, 5.2, 5.9, 6.1, 5.3, 5.7, 5.8, 6.2, 5.4,
        5.6, 6.0, 5.1, 5.9, 5.5, 6.3, 5.2, 5.7, 6.1, 5.4,
        5.8, 5.0, 6.0, 5.6, 5.3, 5.9, 6.2, 5.5, 5.7, 6.1,
        5.4, 5.8, 5.2, 6.0, 5.6, 5.9, 5.1, 6.3, 5.5, 5.7,
        6.1, 5.4, 5.8, 6.0, 5.3, 5.6, 6.2, 5.0, 5.9, 5.5,
        5.7, 6.1, 5.4, 5.8, 6.0, 5.2, 5.6, 5.9, 6.2, 5.3,
        5.5, 6.1, 5.7, 5.0, 5.8, 6.0, 5.4, 5.9, 5.2, 6.3,
        5.6, 5.7, 6.1, 5.5, 5.8, 6.0, 5.3, 5.9, 5.1, 6.2,
        5.4, 5.6, 6.1, 5.7, 5.0, 5.8, 6.0, 5.5, 5.9, 5.2,
        6.2, 5.4, 5.7, 6.1, 5.3, 5.8, 5.6, 6.0, 5.1, 5.9,
        5.5, 6.2, 5.7, 5.4, 5.8, 6.1, 5.0, 5.6, 5.9, 6.0,
        5.3, 5.7, 6.2, 5.5, 5.8, 6.1, 5.4, 5.9, 5.2, 6.0,
        5.6, 5.7, 6.3, 5.5, 5.8, 6.1, 5.3, 5.9, 5.0, 6.2,
        5.4, 5.7, 6.0, 5.6, 5.8, 6.1, 5.2, 5.9, 5.5, 6.3
    ]

    weight = [
        60, 70, 80, 50, 68, 82, 55, 72, 62, 85,
        65, 52, 71, 78, 61, 88, 54, 69, 75, 83,
        59, 67, 48, 73, 86, 56, 70, 79, 63, 81,
        51, 74, 66, 91, 58, 72, 53, 80, 68, 84,
        61, 57, 76, 87, 64, 49, 71, 89, 60, 69,
        78, 62, 55, 75, 84, 58, 72, 70, 90, 61,
        65, 79, 52, 74, 63, 92, 54, 68, 82, 59,
        73, 50, 81, 66, 57, 76, 88, 64, 71, 83,
        60, 75, 53, 80, 67, 77, 51, 94, 62, 70,
        85, 59, 72, 79, 56, 65, 87, 48, 76, 61,
        69, 84, 58, 73, 81, 54, 66, 78, 89, 57,
        63, 86, 71, 50, 74, 80, 60, 77, 53, 91,
        68, 72, 83, 64, 75, 79, 55, 76, 49, 88,
        61, 67, 85, 70, 52, 73, 82, 63, 78, 56,
        87, 60, 71, 84, 58, 74, 69, 80, 51, 77,
        65, 89, 72, 59, 75, 86, 48, 68, 79, 81,
        57, 70, 92, 63, 76, 85, 60, 78, 54, 82,
        67, 73, 90, 65, 74, 83, 56, 77, 50, 88,
        62, 71, 80, 66, 75, 85, 53, 79, 61, 93
    ]

    x, y = data_shuffling(list(weight), list(height))

    # X = Weight
    # Y = Height
    xtr, xt, ytr, yt = train_test_split(x, y, 80)

    m, c = single_LR(xtr, ytr)
    mean_error = testing(xt,yt,m,c)
    mean_squarred_error=mean_error**2
    print(mean_error)
    print(mean_squarred_error)

    while True:
        print("Enter weight for height prediction:")
        x = float(input())

        y = m * x + c

        print(f"Predicted height: {y:.2f} ft")
        print("-" * 40)


if __name__ == "__main__":
    main()