def main():
 A=[1,2,3,4,5,6,7,8,9,10]
 print(len(A))
#remove 
 A.remove(7)
 print(A)
#pop
 A.pop(1)
 print(A) 
#append 
 A.append(11)
 print(A)
#
 b=[0]
 for i in A:
   b.append(i)
   print(b)
if __name__=="__main__":
    main()    