def outer(n1, n2):
    def inner():
        a = n1 - n2 
        return a

    return inner
def add(a,b):
    return outer(12,3)
def main():
    k=outer(13,4)
    a=add((outer(3,1))(),(add(k(),2))())
    print(a())

if __name__=="__main__":
    main()    
