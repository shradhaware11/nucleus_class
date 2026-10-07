a=20
def main():
    global a
    a+=1
    print(a)
    abc()
def abc():
    print(a)
if __name__=="__main__":
    main()  