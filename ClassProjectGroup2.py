################################
# Course: CMPS 3500
# Class Project
# Python Implementation: Basic Data Analysis
# Date: 4/12/2022
# Student 1: Patrick Park
# Student 2: Carlos Hernandez
# Student 3: Edmund Felicidario
# Student 4: Juan Sierra Diaz
################################

######### to-do list ###########
# data cleaning: --> DONE!
# 1. DONE - load csv file and store in array/dataframe
# 2. DONE - eliminate rows with missing data in..(see prompt)
# 3. DONE - eliminate rows with empty values in 3 or more columns
# 4. DONE - eliminate rows with distance zero 
# 5. DONE - only consider in your analysis the first 5 digits of the zip
# 6. DONE - eliminate? rows that lasted no time (endtime - starttime = 0)
#
# functions:
# 1. what month were there more accidents reported?
# 2. what state had most accidents in 2020?
# 3. what state had most accidents with severity 2 in 2021?
# 4. what severity is most common in Virginia?
# 5. what are the 5 cities that had the most accidents in 2019 in CA?
# 6. what was the avg humidity and avg temp of all accidents of severity 4 in 2021?
# 7. what are the 3 most common weather conditions when accidents occured?
# 8. what was the maximum visibility of all accidents of severity 2 in new hampshire?
# 9. how many accidents of each severity were recorded in bakersfield?
# 10. what was the longeset accident (in hours) recorded in florida in spring (mar, apr, may) of 2022?
#
# runtimes
# interfaces
#
###############################

# imports pandas, a useful data science library
import csv
import pandas as pd
import numpy as np
from datetime import date

import datetime

def Question1():

	#print(type(validData["Start_Time"]))
	data['month'] = pd.DatetimeIndex(data['Start_Time']).month
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
	for row in data['month']:
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
data = data.dropna(subset=['ID', 'Severity', 'Zipcode','Start_Time','End_Time','Visibility(mi)', 'Weather_Condition','Country'])

# drop rows with 3 or more missing column values
data = data.dropna(axis=0,thresh=18)

# delete rows with 0 in distance 
data = data.loc[data['Distance(mi)'] != 0]

# converts zipcode data type to string, then shows only the first 5 characters
# this doesnt remove some invalid zipcodes like <4 digit zips
data['Zipcode'] = data['Zipcode'].apply(str)
data['Zipcode'] = data['Zipcode'].str[:5]

# removes rows with endtime-starttime = 0
# does NOT use math; it checks if the strings end/start date are equal and if strings end/start time are equal
data = data.drop(data[(data["End_Time"].str.split(expand=True)[0] == data["Start_Time"].str.split(expand=True)[0]) & (data["End_Time"].str.split(expand=True)[1] == data["Start_Time"].str.split(expand=True)[1])].index)

# resets index numbers, this should be the second to last thing called (last statement should be print)
data.reset_index(drop=True,inplace=True)

# prints all rows after cleanup
print(data)

# print(delta)
#Question1()







