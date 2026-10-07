def gm():
    print("Good Morning!")
def ga():
    print("Good Afternoon!")
def ge():
    print("Good Evening!")
def gn():
    print("Good Night!")

def greet(morning, afternoon,evening,night, hour):
    if 5 <= hour < 12:
        morning()
    elif 12 <= hour < 16:
        afternoon()
    elif (16 <= hour <= 20):
         evening()
    elif  (20 <= hour <=23) or (0<= hour<5):
         night()
    else:
        print("Invalid Time")

def main():
    hour = int(input("Enter hour (0-23): "))
    greet(gm, ga,ge, gn, hour)

if __name__ == "__main__":
    main()