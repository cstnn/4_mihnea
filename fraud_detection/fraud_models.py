import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import sklearn
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model, preprocessing
from sklearn.utils import compute_class_weight
# import matplotlib.pyplot as plt
import shutil
import pickle
import custom

from sklearn import linear_model, preprocessing
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score
import sklearn


# IMPORT dependencies
print(custom.section_start("LOAD dependencies and dataset"))
print(custom.header("Importing dependencies ..."))
print(custom.header("Reading data file ..."))
filename = custom.curr_folder()+"\\fraud_edited.csv"
data = pd.read_csv(filename, low_memory=False)
print(custom.section_end())

print(custom.section_start("Initial DATASET preview"))
print("Total number of entries : "+ str(len(data)))
print(custom.separator())
print(list(data.columns))
print(custom.separator())
print(data.head(2))
print(custom.section_end())


# ENCRYPTING the data
print(custom.section_start("Encrypting the non numerical data"))
print(custom.header("Cloning the file for encryption..."))
shutil.copy(filename, custom.curr_folder()+"\\fraud_edited_encr.csv")

print(custom.header("Opening the cloned file..."))
file = custom.curr_folder()+"\\fraud_edited_encr.csv"

print(custom.header("Reading data file ..."))
raw_data = pd.read_csv(file, sep=",")

print(custom.header("Cleaning up the file ..."))
# raw_data = raw_data.fillna('NaN')
raw_data = raw_data.dropna()
data_le = raw_data

print(custom.header("Encrypting data file ..."))
le = LabelEncoder()
data_le = data_le.apply(le.fit_transform)
print(data_le.head(2))

print(custom.header("Randomizing the order of the lines ..."))
data_le.iloc[np.random.permutation(len(data_le))]
data_le.reset_index(drop=True)
print(custom.section_end())


# Declaring the value to predict and ignore
print(custom.section_start("Preparing training data"))

predict = 'Fraud'
print(custom.header("Separating the value to be predicted ... ["+predict+"]"))

print(custom.header("Marking features (columns) that need to be ignored ..."))
# ignore_1 = 'Pts_1'
# ignore_2 = 'Pts_2'
# ignore_3 = 'Court'
# ignore_4 = 'Round'
# ignore_5 = 'Series'
# ignore_6 = 'Location'
# ignore_7 = 'Year'
# ignore_8 = 'Rank_1'
# ignore_9 = 'Rank_2'
# ignore_10 = ''
# ignore_11 = ''



print(custom.header("Defining Training data..."))
x = np.array(data_le.drop(columns={predict}))
# x = np.array(data_le.drop(columns={predict, ignore_1, ignore_2, ignore_4, ignore_5, ignore_6, ignore_7}))
# x = np.array(data_le.drop(columns={predict, ignore_1, ignore_2, ignore_3, ignore_4, ignore_5, ignore_6, ignore_7}))
# x = np.array(data_le.drop(columns={predict, ignore_1, ignore_2, ignore_3, ignore_4, ignore_5, ignore_6, ignore_7, ignore_8, ignore_9, ignore_10, ignore_11}))

print(custom.header("Defining Testing data..."))
y = np.array(data_le[predict])

def run_class_models(x, y):
    # List of models
    ABC = AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None, learning_rate=1, n_estimators=50, random_state=0)
    GBC = GradientBoostingClassifier(loss='deviance', learning_rate=0.1, n_estimators=100, subsample=1.0, criterion='friedman_mse',
                                    min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3, min_impurity_decrease=0.0, 
                                    min_impurity_split=None, init=None, random_state=None, max_features=None, verbose=0, max_leaf_nodes=None, 
                                    warm_start=False, presort='auto', validation_fraction=0.1, n_iter_no_change=None, tol=0.0001)
    KNC = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=1000)
    LogR = linear_model.LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, solver='lbfgs', max_iter=10000, 
                                        multi_class='auto', verbose=0, warm_start=False, n_jobs=None, l1_ratio=None)
    RFC = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                                max_depth=2, max_features='auto', max_leaf_nodes=None,
                                min_impurity_decrease=0.0, min_impurity_split=None,
                                min_samples_leaf=1, min_samples_split=2,
                                min_weight_fraction_leaf=0.0, n_estimators=1000, n_jobs=None,
                                oob_score=False, random_state=0, verbose=0, warm_start=False)
    XGB = XGBClassifier(random_state=15,learning_rate=0.001)
    OVR_XGB = OneVsRestClassifier(XGBClassifier(random_state=15,learning_rate=0.001))
    OVR_RFC = OneVsRestClassifier(RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                                max_depth=2, max_features='auto', max_leaf_nodes=None,
                                min_impurity_decrease=0.0, min_impurity_split=None,
                                min_samples_leaf=1, min_samples_split=2,
                                min_weight_fraction_leaf=0.0, n_estimators=1000, n_jobs=None,
                                oob_score=False, random_state=0, verbose=0, warm_start=False))
    models = [LogR, XGB, RFC, GBC, KNC, ABC, OVR_XGB, OVR_RFC]
    models_label = ['LogR', 'XGB', 'RFC', 'GBC', 'KNC', 'ABC', 'OVR_XGB', 'OVR_RFC']
    
    # Defining training and testing data
    print(custom.header("Spliting the dataset into Train and Test data..."))
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1, random_state=77)
    print(custom.section_end())
        
    print(custom.section_start("Training multiple models"))
    print(custom.header("Models ") + str(models_label))
    
    i=0
    for model in models :
        
        model.fit(x_train, y_train)
        accuracy = model.score(x_test, y_test)
        print(custom.header("> Accuracy : " + str(round(accuracy*100, 2)) + " %   |   " + str(models_label[i])))
        i=i+1
        if accuracy > 0.9:
            pickle_file = custom.curr_folder() + "\\" + "90+.pickle"
            with open(pickle_file, "wb") as f:
                pickle.dump(model, f)
        

# Running all models
run_class_models(x, y)

print(custom.section_end())
print(custom.copyright())
print(custom.section_end())