def add_four(a=1, b=2, c=3, d=4):
    return a + b + c + d

def main():
    result = add_four(c=10, a=4)
    print(result)

if __name__ == "__main__":
    main()