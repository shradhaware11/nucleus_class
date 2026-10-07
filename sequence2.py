def main():
 A=[1,2,3,4,5,6,7,8,9,10]
 
 print(len(A))
 """for i in range(0,4+1):
    print(A[i])"""
 for i in range(len(A)-1,0,-1):
    print(A[i])
if __name__=="__main__":
    main()    