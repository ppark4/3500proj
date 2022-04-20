# Course: CMPS 3500
# Class Project
# Python Implementation: Basic Data Analysis
# Date: 4/12/2022
# Student 1: Patrick Park
# Student 2: Carlos Hernandez
# Student 3: Edmund Felicidario
# Student 4: Juan Sierra Diaz

# imports pandas, a useful data science library
import csv
import pandas as pd
import numpy as np
from datetime import date

import datetime

def Question1():

	#print(type(validData["Start_Time"]))
	validData['month'] = pd.DatetimeIndex(validData['Start_Time']).month
	#print(validData)
	#df['year'] = pd.datetimeIndex(validData["Start_Time"]).year

	accident_counter_january = 0
	accident_counter_february = 0
	accident_counter_march = 0
	accident_counter_april = 0
	accident_counter_may = 0
	accident_counter_june = 0
	accident_counter_july = 0
	accident_counter_august = 0
	accident_counter_september = 0
	accident_counter_october = 0
	accident_counter_november = 0
	accident_counter_december = 0
	for row in validData['month']:
		if row == 1:
			accident_counter_january = accident_counter_january + 1
		if row == 2:
			accident_counter_february = accident_counter_february + 1
		if row == 3:
			accident_counter_march = accident_counter_march + 1
		if row == 4:
			accident_counter_april = accident_counter_april + 1
		if row == 5:
			accident_counter_may = accident_counter_may + 1
		if row == 6:
			accident_counter_june = accident_counter_june + 1
		if row == 7:
			accident_counter_july = accident_counter_july + 1
		if row == 8:
			accident_counter_august = accident_counter_august + 1
		if row == 9:
			accident_counter_september = accident_counter_september + 1
		if row == 10:
			accident_counter_october = accident_counter_october + 1
		if row == 11:
			accident_counter_november = accident_counter_november + 1
		if row == 12:
			accident_counter_december = accident_counter_december + 1 


	#print(accident_counter_january)
	#print(accident_counter_february)
	#print(accident_counter_march)
	#print(accident_counter_april)
	#print(accident_counter_may)
	#print(accident_counter_june)
	#print(accident_counter_july)
	#print(accident_counter_august)
	#print(accident_counter_september)
	#print(accident_counter_october)
	#print(accident_counter_november)
	#print(accident_counter_december)

	month_list = [accident_counter_january, accident_counter_february,
	accident_counter_march, accident_counter_april, accident_counter_may,
	accident_counter_june, accident_counter_july, accident_counter_august,
	accident_counter_september,accident_counter_october,
	accident_counter_november, accident_counter_december]

	max_month = max(month_list)

	total = sum(month_list)
	#print(total)
	print("The month with most accidents was december with: "), print (max_month)

# reads file
data = pd.read_csv("test_data.csv", index_col=0)
# removes rows with specific missing data
validData = data.dropna(subset=['ID', 'Severity', 'Zipcode','Start_Time','End_Time','Visibility(mi)', 'Weather_Condition','Country'])

#delete rows with 0 in distance 
data.shape
validData = data.loc[data['Distance(mi)'] != 0]
data.shape
#drop rows with 3 or more missing column values
validData = validData.dropna(axis=0,thresh=18)
#remove rows with elapsed time equal to zero
delta = pd.to_datetime(data["End_Time"])-pd.to_datetime(data["Start_Time"])
# resets index numbers
validData.reset_index(drop=True,inplace=True)

# prints all rows after cleanup
print(validData)

print(delta)

Question1()







