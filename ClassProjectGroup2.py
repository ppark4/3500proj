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
	#df['year'] = pd.datetimeIndex(validData["Start_Time"]).year

	# Get the most frequent month
	# The most frequent month should be the month with most accidents
	month_num = data['month'].value_counts().idxmax()


	month_num = str(month_num)

	datetime_object = datetime.datetime.strptime(month_num, "%m")
	full_month_name = datetime_object.strftime("%B")


	print('The month with most accidents was:',full_month_name)

	# Return data to the original format since an extra
	# column was added ("month") to isolate the month
	# and answer the question
	data.drop("month", axis=1, inplace=True)

def Question2():

	data['year'] = pd.DatetimeIndex(data['Start_Time']).year

	
	# Filter data with only the year 2020
	data_2020 = data[data['year'] == 2020]

	state_most_accidents = data_2020['State'].value_counts().idxmax()
	#print (data_2020)

	print('The state with most accidents in 2020 was:', state_most_accidents)


	# Return data to the original format since an extra
	# column was added ("year") to isolate the year
	# and answer the question
	data.drop("year", axis=1, inplace=True)

def Question3():
	#3. what state had most accidents with severity 2 in 2021?


	data['year'] = pd.DatetimeIndex(data['Start_Time']).year

	# Filter data with year 2021 and only states with Severity == 2
	data_2021 = data[(data['year'] == 2021) & (data['Severity'] == 2)]

	states_severity_2 = data_2021['State'].value_counts().idxmax()

	#print(data_2021)

	print('The state with most accidents with severity 2 in 2021 was:', states_severity_2)

	# Return data to the original format since an extra
	# column was added ("year") to isolate the year
	# and answer the question
	data.drop("year", axis=1, inplace=True)


# reads file
data = pd.read_csv("test_data.csv", index_col=0)
#data = pd.read_csv("US_Accidents_data.csv", index_col=0)


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
Question1()


# Had to comment out Question2 and Question 3 because 
# it only works when reading the US_Accidents_data.csv file
#Question2()
#Question3()

#print(data)






