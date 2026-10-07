def main():
 a=int(input("enter the num="))
 fact=1
 for i in range(a,1,-1):
   fact=fact*i
   print(fact)
if __name__=="__main__":
  main()