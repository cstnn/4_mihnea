# ---------- Importing standard libraries
from datetime import datetime
import os
import pickle
# ---------- Importing SKLEARN models
from sklearn import linear_model, preprocessing
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score
import sklearn


# GET FOLDER
def curr_folder():
    foldername = os.path.dirname(os.path.realpath(__file__))
    return foldername

# PROGRESS INDICATOR
def progress(perc, step):
    if perc == 0:
        return "-----------------------------------------\n"+"[__________] 00% | "+ step +"\n-----------------------------------------"
    if perc == 20:
        return "-----------------------------------------\n"+"[::________] 20% | "+ step +"\n-----------------------------------------"
    if perc == 40:
        return "-----------------------------------------\n"+"[::::______] 40% | "+ step +"\n-----------------------------------------"
    if perc == 60:
        return "-----------------------------------------\n"+"[::::::____] 60% | "+ step +"\n-----------------------------------------"
    if perc == 80:
        return "-----------------------------------------\n"+"[::::::::__] 80% | "+ step +"\n-----------------------------------------"
    if perc == 100:
        return "-----------------------------------------\n"+"[::::::::::] 100% | "+ step +"\n-----------------------------------------"
    if perc == 69:
        return "-----------------------------------------\n"+"[::ERROR!::] !!! | "+ step +"\n-----------------------------------------"


# HEADER
def header(section):
    return "-------------------" + ":: " + section


# SECTION
def section_start(section):
    return "---------------------------------------------------------------------------------------\n" + ":: " + section + " ::" +"\n---------------------------------------------------------------------------------------"

def section_end():
    return "----------------------------------------///--------------------------------------------\n"


# SUB-SECTION
def subsection_start(section):
    return "---------------------------------------------\n" + ":: " + section + " ::" +"\n---------------------------------------------"

def subsection_end(section):
    return "--------------------///---------------------\n"


# SEPARATOR
def separator_small():
    return "-----------------------------------------"

def separator():
    return "---------------------------------------------------------------------------------------"


# SPACER
def spacer():
    return "\n\n\n\n\n\n"


# COPYRIGHT
def copyright():
    return "---------------------------------------------------------------------------------------\n:::::: COPYRIGHT (c) Costin Nadolu aka </cstn> ::::::"


# DATASET CLEANUP
def cleanup(dataset):
    raw_data = raw_data.fillna('NaN')
    raw_data = raw_data.dropna()
