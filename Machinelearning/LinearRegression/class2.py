class Human:

    def __init__(self,name,f_name,m_name,l_name):
        self.name=name
        self.f_name=f_name
        self.m_name=m_name
        self.l_name = l_name
        print("Hello OOP")


def main():
    obj = Human("shradha","raosaheb","pushpalata","w")
    shradha =Human("shradha","raosaheb","pushpalata","ware") 
    print(obj.name)
    print(obj.f_name)
    print(obj.m_name)
    print(obj.l_name)
    print(shradha.name)
    print(shradha.f_name)
    print(shradha.m_name)
    print(shradha.l_name)

if __name__ == "__main__":
    main()