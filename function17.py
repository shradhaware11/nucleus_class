def add(a, **data):
    """this func is used to add 2 nums 
    parameters `a:int`,`b:int`
    return a+b
    """
    print("a =", a)
    print("data =", data)

def main():
    add(1, b="shradha")
    print(add.__doc__)

if __name__ == "__main__":
    main()