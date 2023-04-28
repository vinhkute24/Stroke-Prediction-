import pandas as pd 
import numpy as np 

from sklearn.model_selection import train_test_split


df = pd.read_csv (r'C:\Users\rog-g\OneDrive\Desktop\Lab - Introduction to Data Mining\Project_python\healthcare-dataset-stroke-data.csv', header =0)

data1 = df.drop(columns=['id'], inplace=True)


print(data1)


X = df.drop("stroke", axis=1)
y = df["stroke"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 


print("\n")
print(" Length of data frame: " , len(df),"\n","Length of data train: ",len(X_train),"\n","Length of data test: ", len(X_test))
print("\n")

data_splits = [X_train,X_test]

def median_filler(split): 

    split["bmi"].fillna(split["bmi"].median(),inplace=True)
    
for split in data_splits:
    median_filler(split)
    print(f"Number of nulls: {split['bmi'].isnull().sum()}")

    print(f"Datatypes:\n{split.dtypes}")
    print("__________________________________")


train_data = pd.concat([X_train, y_train], axis=1)
train_data.to_excel (r'DataTrain.xlsx', index = None, header=True)
train_data.to_csv (r'DataTrain.csv', index = None, header=True) 

test_data = pd.concat([X_test, y_test], axis=1)
test_data.to_excel (r'DataTest.xlsx', index = None, header=True)
test_data.to_csv (r'DataTest.csv', index = None, header=True) 

df.to_excel (r'DataFrame.xlsx', index = None, header=True)



