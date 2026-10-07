class Abc:

    def __init__(self):
        self.f_name = "AGG"
        self.age = 18
        self.town = "Pune"
        self._insta_password = "HelloWorld"


def main():
    obj = Abc()
    print("encapsulated data cant be accesed directly")
    print(obj._Abc__insta_password)

    print("encapsulated  data can be accesed by add _<class name before variable name>")
if __name__ == "__main__":
    main()