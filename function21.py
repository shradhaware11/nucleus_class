def decorator(func):
    def pretty(n):
        data = func(n)

        for i in range(0,len(data)):
            print(f"\nStudent {i}")
            print("__________________")
            print("Name :", data[i]["Name"])
            print("Age :", data[i]["Age"])
            print("Marks :", data[i]["Marks"])
            print("__________________")
    return pretty
@decorator
def std_data(n):
    d=[]
    for i in range(0,n):
        student = {}

        student["Name"] = input("Enter Name: ")
        student["Age"] = int(input("Enter Age: "))
        student["Marks"] = float(input("Enter Marks: "))

        d.append(student)

    return d

def main():
  n=int(input("enter no of students="))
  s=std_data(n)
  


if __name__=="__main__":
    main()    