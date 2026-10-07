import datetime

def decorator1(func):
    def data_time():
        print(func())
        print(datetime.datetime.now())
    return data_time

@decorator1
def gm():
    return "Good Morning"

def main():
    gm()

if __name__ == "__main__":
    main()