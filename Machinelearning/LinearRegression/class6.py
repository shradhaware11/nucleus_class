class car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def run(self, speed):
        if self.brand == "suzuki":
            print(self.model, "hya speed ne palu shakat nahi")

        elif self.brand == "mercedes":
            print(self.model, "is running at", speed)

    def modify(self, brand):
        self.brand = brand

    def wheels(self):
        print("4 chaki")


def main():

    maruti = car("suzuki", "wagonar")
    maruti.run(110)

    benz = car("mercedes", "cla")
    benz.wheels()
    benz.run(110)

    print(maruti.brand)

    maruti.modify("toyota")

    print(maruti.brand)


if __name__ == "__main__":
    main()