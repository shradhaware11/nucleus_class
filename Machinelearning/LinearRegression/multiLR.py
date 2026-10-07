import numpy as np
def data():
    x=[[5,6,5.5],[60,65,50]]
    y=[25,24,20]
    return x,y

def multiLR(x_independent,y_dependent):
    once=[[1 for i in y_dependent]]
    x=once+x_independent
    x_transpose=np.array(x) 
    x=x_transpose.T
    y=np.array(y_dependent)
    #(((x^T)*x)^-1)*((x^T)*y)
    #step 1:((x^t*x))
    xT_x_product=x_transpose @ x
    #step 2:(x^t*x)^-1
    xT_x_product_inverse=np.linalg.inv(xT_x_product)
    #step 3:(x^t*y)
    xT_y_product=x_transpose @ y
    #final step ((x^t*x)^-1) * (x^t*y)
    bx=xT_x_product_inverse @xT_y_product
    return tuple(bx)
def testing(x_test,y_test,bx):
    height=x_test[0]
    weight=x_test[1]
    error=0

    for i in range(0,len(x_test)):
        yp=bx[0]+bx[1]*height[i]+bx[2]*weight[i]
        error+=y_test[i]-yp

    return error/len(y_test)
def main():
    x,y=data()
    b=multiLR(x,y)
    
    line="-"*50
    print(line)
    print("enter weight")
    weight=float(input())
    print("enter height")
    height=float(input())  
    yp=b[0]+b[1]*(height)+b[2]*(weight)
    print("your prediction is",yp)
    print(line)
    error = testing(x, y, b)
    print("Error:", error)

if __name__=='__main__':
    main();