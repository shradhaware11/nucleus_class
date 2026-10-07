class god:

    name = "vishnu"

    def __init__(self, birth_name):
        print("Name of krushna before birth:", self.name)
        print("cry")
        self.name = birth_name
        print("Name of krushna after birth:", self.name)


class bramha:

    gun = ["talks truth", "dont afraid", "doesnt go on the wrong path"]

    def __init__(self):
        pass

    def show_gun(self):
        for points in self.gun:
            print(points)


class human(bramha):

    def __init__(self, name, f_name, m_name, l_name):
        self.name = name
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name

    def current_human_gun(self):

        print("Have you ever lie:")
        if input().lower() == "yes":
            self.first_gun = True
        else:
            self.first_gun = False

        print("Do you afraid:")
        if input().lower() == "yes":
            self.second_gun = True
        else:
            self.second_gun = False

        print("Have you ever choosen wrong path:")
        if input().lower() == "yes":
            self.third_gun = True
        else:
            self.third_gun = False

        print("These are the thoughts you got from bramha. "
              "Check whether it does match with your answer")

        self.show_gun()


def main():

    krushna = god("krushna")

    yash = human("yashraj", "arunrao", "sushma", "deshmukh")

    yash.current_human_gun()


if __name__ == "__main__":
    main()