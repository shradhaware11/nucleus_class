def table(no):

    for i in range(1,11):
       yield no*i

def main():

   for i in table(3):
      print(i)

if __name__=="__main__":
 main()