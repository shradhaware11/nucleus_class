def main():
    a="shradha"
    print(a[2:6:2])
    print(a[0:4:2])
    print(a[1])
    print(a[0:3])
    print(a[:])
    a="hello"
    print(a[5::-1])
    b="hello i am shradha"
    b=b.split(" ")
    print(b[0:3][-1::-1])
if __name__=="__main__":
    main()
