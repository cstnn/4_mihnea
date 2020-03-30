# Import library for data manipulation (dataframe)
import pandas as pd
# Import library for complex numerical operations
import numpy as np
# Import library for Macine Learning
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
# Import library for saving the Model output
import pickle
# Import library for CSV file import an parsing
import csv
# Import library for Windows file management
import shutil
# Import library for date-time management
from datetime import datetime

print("\n:::::::: Starting the program...")
print("------------------------------------------------")
print("::: [DONE !] Imported all dependencies... ")
print("------------------------------------------------")

# Reading raw data from CSV file
data = pd.read_csv("C:\\Costin\\_python\\__workshop\\1_ml_student_grade\\student_data.csv", sep=",")
# data = pd.read_csv("student_data.csv", sep=",")

# Displaying Header and few lines to preview the data content
print("::: Data sample :\n", data.head())

## Encrypting the categorical values (where needed - where non-numerical values exist)
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# data = data.apply(le.fit_transform)
# print(data.head())

# Defining variable to predict
print("------------------------------------------------")
predict = 'final_grade'
print("::: Predicting variable : ", predict)

# Defining Training and Validation data - X = Training data / Y = Validation data
x = np.array(data.drop(columns={predict}))
y = np.array(data[predict])

# Defining Training and Testing data - Split the data from the file into Train and Test
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.3)

# Defining what Machine Learning model we want to use
model = linear_model.LinearRegression()
model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)
print("> Accuracy : " + str(accuracy*100) + " % ")
print("------------------------------------------------")

# Saving the ML model output to a file so it can be used without the training part
with open("C:\\Costin\\_python\\__workshop\\1_ml_student_grade\\student_data_model.pickle", "wb") as f:
    pickle.dump(model, f)
print("::: [DONE !] Saved the Machine Learning model pickle... ")

# Displaying a predictions for the first 10 lines from the original dataset
predictions = model.predict(x_test)
print("::: List of column headers from the model inputs: \n", list(data.columns))

print("------------------------------------------------")
print("::: Here are some samples predictions from the TEST dataset:")
for x in range(2,7):
    # print("Reality: ", y_test[x] , " |> ", "Prediction: ", int(predictions[x]))
    print("> Input: ", x_test[x], "\n>", "Reality: ", y_test[x] , " |> ", "Prediction: ", predictions[x], " >> Delta = ", predictions[x]-y_test[x], "\n")
print("---------------------///------------------------")
