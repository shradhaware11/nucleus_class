a=20
def main():
 global a
 abc()
 del a
 
def abc():
    print(a)
if __name__=="__main__":
    main()    