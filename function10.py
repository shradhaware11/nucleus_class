No=0
def hello():
 global No
 print("hello",No)
 No+=1
 return hello()    
def main():
 hello()

if __name__=="__main__":
 main()
