class human:

    def __init__(self, name, f_name, m_name, l_name):
        self.name = name
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        print("cry")

    def drink(self,food):
        print(self.name,"having a",food)
def main():

    obj = human("shradha", "raosaheb", "pushpalata", "ware")

    print(obj.name)
    obj.drink("milk")


if __name__ == "__main__":
    main()