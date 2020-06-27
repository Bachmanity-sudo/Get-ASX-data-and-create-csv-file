# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:03:20 2020
Bachmanity Insanity Productions 2020
"""
import fileinput
import glob
import pandas as pd
from datetime import datetime
import zipfile
import os
import errno
import shutil

#updates 1.2
#unzips files

####set variables: location of zipped files
ZipDir = ("C:/ASX_DATA/ZIPPED/") #/ requried after final folder

####

#set sub dirs
TempDir = (ZipDir + "Temp/")
TxtDir = (ZipDir + "Txt/")
CurrentDir = os.getcwd() #save current working directory

# Create temp directory if it doesn't exist
try:
    os.makedirs(TempDir)    
    print("Directory " , TempDir ,  " Created ")
except FileExistsError:
    print("Directory " , TempDir ,  " already exists")

# Create txt directory if it doesn't exist
try:
    os.makedirs(TxtDir)    
    print("Directory " , TxtDir ,  " Created ")
except FileExistsError:
    print("Directory " , TxtDir ,  " already exists")

# change Dirs
os.chdir(ZipDir)

#unzip multiple files
extension = ".zip"
for item in os.listdir(ZipDir): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(TempDir) # extract file to dir
        zip_ref.close() # close file

#remove MAC folder
try:
    shutil.rmtree(TempDir + "__MACOSX")
except FileNotFoundError:
    print(TempDir + "__MACOSX not found")

#copy txt files in single folder
for path, subdirs, files in os.walk(TempDir):
    for name in files:
        filename = os.path.join(path, name)
        shutil.copy2(filename, TxtDir)

#create list of txt files
file_list = glob.glob(TxtDir + "*.txt")

os.chdir(CurrentDir) #change to starting working directory

#merge txt files into single txt file
with open('ASX_DATA.txt', 'w') as file:
    input_lines = fileinput.input(file_list)
    file.writelines(input_lines)

#open txt file and save as dataframe
data = pd.read_csv('ASX_DATA.txt', sep=",")
data.columns = ["Ticker","Date","Open", "High", "Low", "Close", "Volume"]

#convert date string to datetime format
#data['Date'] = pd.to_datetime(data['Date'].astype(str), format='%Y%m%d')
data['Date'] = pd.to_datetime(data['Date'].astype(str))
data["Date"] = data["Date"].dt.strftime('%d/%m/%Y') #change date format

#save data as csv file
data.to_csv("ASX_DATA.csv", sep=',', index=False)
print("Saved ASX_DATA.csv and ASX_DATA.txt in:  " + CurrentDir)
