import numpy as np
def main():
  m1=np.array([[2,2],[2,2]])
  m2=np.array([[4,4],[4,4]])

  line="-"*50
  print(line)
  #matrix multiplication
  multiplication =m1@m2
  print(multiplication)
  m3=np.array([[3,2,3],[4,5,6],[7,8,9]])
  m3_transpose=m3.T
  print("transpose of m3 =\n",m3_transpose)
  print(line)
  m3_inverse =np.linalg.inv(m3)
  print("inverse of m3 =\n",m3_inverse)
if __name__=='__main__':
    main();