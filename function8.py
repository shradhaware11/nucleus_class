def add(a: int, b: int, *c):
    print(a)
    print(b)
    print(c)

def main():
    add(10, 11, 21, 31, 33)

if __name__ == "__main__":
    main()