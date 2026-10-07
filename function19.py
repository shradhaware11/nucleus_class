import datetime
def date_time(func):
 print(func())
 print(datetime.datetime.now())


def gm():
    return("good morning")
def main():
 date_time(gm)
if __name__=="__main__":
   main()        