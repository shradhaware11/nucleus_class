def outer(n1, n2):
    add = n1 + n2
    print("Addition =", add)

    def inner(n3):
        global p
        a = n1 - n2 + n3
        p += 1
        return a

    return inner

def main():
    func = outer(2, 8)
    print(func(9))

if __name__ == "__main__":
    main()