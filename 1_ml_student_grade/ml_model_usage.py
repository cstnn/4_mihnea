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


# Reading data from ML model pickle
pickle_in = open('C:\\Costin\\_python\\__workshop\\1_ml_student_grade\\student_data_model.pickle', "rb")
model = pickle.load(pickle_in)
print("::: [DONE !] Model loaded from Pickle file !")
print("------------------------------------------------")

# Estimating the final student grade for a new student (not present in the initial dataset)
print("::: Predicting final grade for a student with the below data :")
data_ad_hoc = [[5,6,7]]
selective = model.predict(data_ad_hoc)
print("Raw data   > ", data_ad_hoc)
print("Prediction > ", selective)
print("---------------------///------------------------")