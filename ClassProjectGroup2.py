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
# 10. what was the longeset accident (in hours) recorded in florida in spring (mar, apr, may) of 2020?
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

# 1. what month were there more accidents reported?
def Question1():

	# Create an extra column with each indivual month
	data['month'] = pd.DatetimeIndex(data['Start_Time']).month
	
	# Get the most frequent month
	# The most frequent month should be the month with most accidents
	month_num = data['month'].value_counts().idxmax()


	month_num = str(month_num)

	datetime_object = datetime.datetime.strptime(month_num, "%m")
	full_month_name = datetime_object.strftime("%B")


	print(" ")
	print("1. what month were there more accidents reported?")
	print('The month with most accidents was:',full_month_name)

	# Return data to the original format since an extra
	# column was added ("month") to isolate the month
	# and answer the question
	data.drop("month", axis=1, inplace=True)

# 2. what state had most accidents in 2020?
def Question2():

	# Create an extra column with each indivual year
	data['year'] = pd.DatetimeIndex(data['Start_Time']).year

	
	# Filter data with only the year 2020
	data_2020 = data[data['year'] == 2020]

	state_most_accidents = data_2020['State'].value_counts().idxmax()

	print(" ")
	print("2. what state had most accidents in 2020?")
	print("The state with most accidents in 2020 was:", state_most_accidents)


	# Return data to the original format since an extra
	# column was added ("year") to isolate the year
	# and answer the question
	data.drop("year", axis=1, inplace=True)

# 3. what state had most accidents with severity 2 in 2021?
def Question3():

	data['year'] = pd.DatetimeIndex(data['Start_Time']).year

	# Filter data with year 2021 and only states with Severity == 2
	data_2021 = data[(data['year'] == 2021) & (data['Severity'] == 2)]

	states_severity_2 = data_2021['State'].value_counts().idxmax()

	print(" ")
	print("3. what state had most accidents with severity 2 in 2021?")
	print('The state with most accidents with severity 2 in 2021 was:', states_severity_2)

	# Return data to the original format since an extra
	# column was added ("year") to isolate the year
	# and answer the question
	data.drop("year", axis=1, inplace=True)

# 4. what severity is most common in Virginia?
def Question4():
    
	# Filter data with only the state of Virginia
	data_virginia = data[(data['State'] == 'VA')]

	#print(data_virginia)

	# Get the most common severity
	most_common_severity = data_virginia['Severity'].value_counts().idxmax()

	print(" ")
	print("4. what severity is most common in Virginia?)")
	print('The most coomon accident severity in Virginia is: ', most_common_severity)

#5. what are the 5 cities that had the most accidents in 2019 in CA?
def Question5():

	data['year'] = pd.DatetimeIndex(data['Start_Time']).year

	# Filter data with the year 2019 and state CA only
	data_2019_CA = data[(data['year'] == 2019) & (data['State'] == 'CA')]

	# Get the top 5 cities from filtered data
	top_five_cities = data_2019_CA['City'].value_counts().nlargest(5)

	print(" ")
	print("5. what are the 5 cities that had the most accidents in 2019 in CA?")
	print('The 5 cities that had the most accidents in 2019 in CA are: ')
	print(top_five_cities.to_string()) 

	# Return data to the original format since an extra
	# column was added ("year") to isolate the year
	# and answer the question
	data.drop("year", axis=1, inplace=True)


#6. what was the avg humidity and avg temp of all accidents of severity 4 in 2021?
def Question6():


 	data['year'] = pd.DatetimeIndex(data['Start_Time']).year

 	# Filter data
 	data_2021_Severity_4 = data[(data['year'] == 2021) & (data['Severity'] == 4)]

 	humidity_sum = data_2021_Severity_4['Humidity(%)'].sum()
 	temperature_sum = data_2021_Severity_4['Temperature(F)'].sum()

 	length_humidity = len(data_2021_Severity_4['Humidity(%)'])
 	length_tem = len(data_2021_Severity_4['Temperature(F)'])

 	humidity_ave = humidity_sum/length_humidity
 	temperature_ave = temperature_sum/length_tem

 	print(" ")
 	print("6. What was the avg humidity and avg temp of all accidents of severity 4 in 2021?")
 	print("The average humidity for all accidents of severity 4 in 2021 is:", humidity_ave)
 	print("The average temperature for all accidents of severity 4 in 2021 is:", temperature_ave)

 	# Return data to the original format since an extra
	# column was added ("year") to isolate the year
	# and answer the question
 	data.drop('year', axis=1, inplace=True)


# 7. what are the 3 most common weather conditions when accidents occured?
def Question7():

	three_common_weather_condtions = data['Weather_Condition'].value_counts().nlargest(3)

	print(" ")
	print("# 7. what are the 3 most common weather conditions when accidents occured?")
	print('The 3 most common weather conditions when accidents occured are: ')
	print(three_common_weather_condtions.to_string())


# 8. what was the maximum visibility of all accidents of severity 2 in new hampshire?
def Question8():

	# Filter data with accidents of New Hampshire with severity 2 
	data_severity_2_NH = data[(data['Severity'] == 2) & (data['State'] == 'NH')]

	data_max_visibility = data_severity_2_NH[data_severity_2_NH['Visibility(mi)'] == 10.0]

	print(" ")
	print("8. What was the maximum visibility of all accidents of severity 2 in new hampshire?")
	print("The following is a dataframe with all accidents with visibility 10")
	print(data_max_visibility)

# 9. how many accidents of each severity were recorded in bakersfield?
def Question9():


	#Filter data to only the city of Bakersfield
	data_Bakersfield = data[(data['City'] == 'Bakersfield')]
	num_accidents = data_Bakersfield['Severity'].value_counts()

	print(" ")
	print("# 9. how many accidents of each severity were recorded in bakersfield?")
	print("The number of accidents of each severity recorded in Bakersfield are as follows: ")
	print(num_accidents.to_string())

# 10. what was the longeset accident (in hours) recorded in florida in spring (mar, apr, may) of 2020?
def Question10():

	# Adding two extra columns to the data to filter based on year and month
	data['year'] = pd.DatetimeIndex(data['Start_Time']).year
	data['month'] = pd.DatetimeIndex(data['Start_Time']).month

	data['Start_Time'] = pd.to_datetime(data['Start_Time'], errors='coerce')
	data['End_Time'] = pd.to_datetime(data['End_Time'], errors='coerce')

	data['Duration'] = (data['End_Time'] - data['Start_Time']).dt.total_seconds() / 60 / 60

	# Filter data with only the year 2020 and Florida
	data_florida = data[(data['year'] == 2020) & (data['State'] == 'FL')] 

	# Further filtering with the spring months(mar,apr,may)
	data_florida_spring = data_florida[(data_florida['month'] == 3) | (data_florida['month'] == 4) | (data_florida['month'] == 5)]


	longest_accident = data_florida_spring['Duration'].max()



	accident_id = data_florida_spring.loc[data_florida_spring['Duration'] == longest_accident]


	print(" ")
	print("10. what was the longeset accident (in hours) recorded in florida in spring (mar, apr, may) of 2020?")
	print("The longest accident (in hours) in Florida during the spring took: ", longest_accident)
	print("Here is the full accident information: ")
	print(accident_id)

	# Return data to orignal format
	data.drop('month', axis=1, inplace=True)
	data.drop('year', axis=1, inplace=True)
	data.drop('Duration', axis=1, inplace=True)

 
print("Loading and cleaning input data set:")
print("************************************")
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

Question1()


# Had to comment out Questions because 
# it only works when reading the US_Accidents_data.csv file
#Question2()
#Question3()
#Question4()
#Question6()
#Question5()
#Question7()
#Question8()
#Question9()
#Question10()


#print(data)
