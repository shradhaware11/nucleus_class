def main():
  a=int(input("enter age="))
  if a<18 and a>0 and a<110:
   print("restricted")
  else:
   print("not restricted")    

if __name__=="__main__":
    main()