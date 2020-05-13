# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:03:20 2020
Bachmanity Insanity Productions 2020
"""
import fileinput
import glob
import pandas as pd

### Set variables
f = "C:/ASX_DATA/DATA/*.txt" #location of daily .txt files
t = "ASX_DATA.txt" #name of merged .txt file
###

#create list of txt files
file_list = glob.glob(f)

#merge txt files into single txt file
with open(t, 'w') as file:
    input_lines = fileinput.input(file_list)
    file.writelines(input_lines)

#open txt file and save as dataframe
data = pd.read_csv(t, sep=",")
data.columns = ["Ticker","Date","Open", "High", "Low", "Close", "Volume"] #name columns

#convert date string to datetime format
data['Date'] = pd.to_datetime(data['Date'].astype(str))
data["Date"] = data["Date"].dt.strftime('%d/%m/%Y') #change date format

#save data as csv file
data.to_csv("ASX_DATA.csv", sep=',', index=False)

