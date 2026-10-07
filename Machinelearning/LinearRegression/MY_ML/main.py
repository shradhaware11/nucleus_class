# DEPENDENCIES
import pandas as pd


class build_model:

    def __init__(self, data_location):
        self.data_location = data_location
        self.df = None
    def cleaning(self):
        pass

    def EDA(self):
        df=pd.read_csv(self.data_location)

        line="-"*64
        print(line)
        print("  EDA starts here")
        print(line)

        print("\n\n")
        print(" 1.Frist 5 entries of data")
        print(line)

        print(df.head(10))

        print("\n\n")
        print(" 2.size/shape of data")
        print(line)
        print(df.shape)

        print("\n\n")
        print("  3.info of data")
        print(line)
        df.info()

        print("\n\n")
        print("4 statistical info of data")
        print(df.describe())

        print("\n\n")
        print("5.  Null report")
        print(line)
        print(df.isnull().sum())

        null_count =df.isnull().sum()

        for i in null_count:
         df[i] = df[i].fillna(df[i].mean())

        print(line)
        print(" EDA ENDS HERE NULL VALUES ARE FILLED WITH MEAN OF THAT COLUMN")
            
        
        

                      

# ENTRY POINT FUNCTION USING ONLY FOR METHODS AND FUNCTION TESTING
def main():
    model = build_model("BMI.csv")
    model.EDA()


if __name__ == '__main__':
    main()