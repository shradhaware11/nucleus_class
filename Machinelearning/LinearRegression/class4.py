class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def run(self,speed):
     if self.brand =="suzuki":
        print(self.model,"hya spped ne palu shakat nahi")

     elif self.brand == "mercedes":
        print(self.model,"is running at",speed)   
def main():
    maruti=car("suzuki","wagonar")
    maruti.run(110)
    benz =car("mercedes","cla")
    benz.run(110)

if __name__=='__main__':
    main();