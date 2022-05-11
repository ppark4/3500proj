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
# ** general issue: tiebreakers return only 1 value instead of all tied values
# 1. DONE - what month were there more accidents reported?
# 2. DONE - what state had most accidents in 2020?
# 3. DONE - what state had most accidents with severity 2 in 2021?
# 4. DONE - what severity is most common in Virginia?
# 5. DONE(issue: extra return value) - are the 5 cities that had the most accidents in 2019 in CA?
# 6. DONE - what was the avg humidity and avg temp of all accidents of severity 4 in 2021?
# 7. DONE(issue: formatting) - what are the 3 most common weather conditions when accidents occured?
# 8. what was the maximum visibility of all accidents of severity 2 in new hampshire?
# 9. DONE(issue: formatting) how many accidents of each severity were recorded in bakersfield?
# 10. DONE - what was the longest accident (in hours) recorded in florida in spring (mar, apr, may) of 2020?
#
# runtimes:
# ** to print current time, use: 
# 		print('[{}] type something here'.format(time()))
# 			--outputs--> "[12:41:34.4949] type something here"
# 1. DONE - Function that returns current time
# 2. IN PROGRESS - Function that returns total runtime
#
# user interface:
# 1. DONE - Load data 
# 2. DONE - Process data
# 3. Answering questions
# 4. Search accidents by city, state, zip
# 5. Search accidents by year, month, day
# 6. Search accidents by temperature, range, visibility
# 7. DONE - Quit
###############################

# imports pandas, a useful data science library
import csv
import time
import pandas as pd
import numpy as np
from datetime import date
import datetime
from datetime import datetime
from timeit import default_timer as timer

startofcode = timer()
# initialize empty dataframe
data = pd.DataFrame()

# filename
file = "test_data.csv"

# current time
def ctime():
    currentTime = datetime.utcnow().strftime('%H:%M:%S.%f')[:-2]
    return currentTime

# load data function, returns loaded dataframe object
def loadData(filename):
    data = pd.read_csv(filename, index_col=0)
    return data

# process data function, returns processed dataframe object
def processData(dataObj):
    # removes rows with specific missing data
    data = dataObj.dropna(subset=['ID', 'Severity', 'Zipcode','Start_Time','End_Time','Visibility(mi)', 'Weather_Condition','Country'])

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

    data.to_csv('sfoo.csv')

    return data

# 1. what month were there more accidents reported?
def Question1(data):

    # Create an extra column with each indivual month
    data['month'] = pd.DatetimeIndex(data['Start_Time']).month
    
    # Get the most frequent month
    # The most frequent month should be the month with most accidents
    month_num = data['month'].value_counts().idxmax()


    month_num = str(month_num)

    datetime_object = datetime.strptime(month_num, "%m")
    full_month_name = datetime_object.strftime("%B")


    #print(" ")
    #print("1. what month were there more accidents reported?")
    #print('The month with most accidents was:',full_month_name)

    # Return data to the original format since an extra
    # column was added ("month") to isolate the month
    # and answer the question
    # data.drop("month", axis=1, inplace=True)

    return full_month_name

# 2. what state had most accidents in 2020?
def Question2(data):
    # issue: only returns the state with lowest index number if tied

    # Create an extra column with each indivual year
    data['year'] = pd.DatetimeIndex(data['Start_Time']).year

    
    # Filter data with only the year 2020
    data_2020 = data[data['year'] == 2020]
    if data_2020.empty:
        return "None"
    else:
        state_most_accidents = data_2020['State'].value_counts().idxmax()
        return state_most_accidents
    #print(" ")
    #print("2. what state had most accidents in 2020?")
    #print("The state with most accidents in 2020 was:", state_most_accidents)


    # Return data to the original format since an extra
    # column was added ("year") to isolate the year
    # and answer the question
    #data.drop("year", axis=1, inplace=True)

# 3. what state had most accidents with severity 2 in 2021?
def Question3(data):

    data['year'] = pd.DatetimeIndex(data['Start_Time']).year

    # Filter data with year 2021 and only states with Severity == 2
    data_2021 = data[(data['year'] == 2021) & (data['Severity'] == 2)]
    if data_2021.empty:
        return "None"
    else:
        states_severity_2 = data_2021['State'].value_counts().idxmax()
        return states_severity_2

    # Return data to the original format since an extra
    # column was added ("year") to isolate the year
    # and answer the question
    #data.drop("year", axis=1, inplace=True)
    #print(type(data_2021))
    #return states_severity_2


# 4. what severity is most common in Virginia?
def Question4(data):
    
    # Filter data with only the state of Virginia
    data_virginia = data[(data['State'] == 'VA')]

    #print(data_virginia)
    if data_virginia.empty:
        return "None"
    else:
        # Get the most common severity
        most_common_severity = data_virginia['Severity'].value_counts().idxmax()
        return most_common_severity


#5. what are the 5 cities that had the most accidents in 2019 in CA?
def Question5(data):

    data['year'] = pd.DatetimeIndex(data['Start_Time']).year

    # Filter data with the year 2019 and state CA only
    data_2019_CA = data[(data['year'] == 2019) & (data['State'] == 'CA')]
    if data_2019_CA.empty:
        return "None"
    else:
        # Get the top 5 cities from filtered data
        top_five_cities = data_2019_CA['City'].value_counts().index.tolist()[:5]

        result = top_five_cities[0] + ", " + top_five_cities[1] + ", " + top_five_cities[2] + ", " + top_five_cities[3] + ", " + top_five_cities[4]

        return result

    #print(" ")
    #print("5. what are the 5 cities that had the most accidents in 2019 in CA?")
    #print('The 5 cities that had the most accidents in 2019 in CA are: ')
    #print(top_five_cities.to_string()) 
    # Return data to the original format since an extra
    # column was added ("year") to isolate the year
    # and answer the question
    #data.drop("year", axis=1, inplace=True)


#6. what was the avg humidity and avg temp of all accidents of severity 4 in 2021?
def Question6(data):

    data['year'] = pd.DatetimeIndex(data['Start_Time']).year

     # Filter data
    data_2021_Severity_4 = data[(data['year'] == 2021) & (data['Severity'] == 4)]

    if data_2021_Severity_4.empty:
        return "None"
    else:
        humidity_sum = data_2021_Severity_4['Humidity(%)'].sum()
        temperature_sum = data_2021_Severity_4['Temperature(F)'].sum()
        
        length_humidity = len(data_2021_Severity_4['Humidity(%)'])
        length_tem = len(data_2021_Severity_4['Temperature(F)'])

        humidity_ave = humidity_sum/length_humidity
        temperature_ave = temperature_sum/length_tem


        result = "Average Humidity: " + str(round(humidity_ave,2)) + " F, " + "Average Temperature: " + str(round(temperature_ave,2)) + "%"

        return result
     #print(" ")
     #print("6. What was the avg humidity and avg temp of all accidents of severity 4 in 2021?")
     #print("The average humidity for all accidents of severity 4 in 2021 is:", humidity_ave)
     #print("The average temperature for all accidents of severity 4 in 2021 is:", temperature_ave)

     # Return data to the original format since an extra
    # column was added ("year") to isolate the year
    # and answer the question
     #data.drop('year', axis=1, inplace=True)


# 7. what are the 3 most common weather conditions when accidents occured?
def Question7(data):

    # Had to create a copy of the orignal data, for some reason I was getting
    # an error when working with the origal data.
    # This seem to work for now, further optimization might be need. 
    temp_df = data

    if temp_df.empty:
        return "None"
    else:
        # Getting three most common weather conditions
        three_common_weather_conditions = temp_df['Weather_Condition'].value_counts().index.tolist()[:3]
        result = three_common_weather_conditions[0] + ", " + three_common_weather_conditions[1] + ", " + three_common_weather_conditions[2]
        return result


    #print(" ")
    #print("# 7. what are the 3 most common weather conditions when accidents occured?")
    #print('The 3 most common weather conditions when accidents occured are: ')
    #print(three_common_weather_conditions.to_string())


# 8. what was the maximum visibility of all accidents of severity 2 in new hampshire?
def Question8(data):

    
    # Filter data with accidents of New Hampshire with severity 2 
    data_severity_2_NH = data[(data['Severity'] == 2) & (data['State'] == 'NH')]

    #data_max_visibility = data_severity_2_NH[data_severity_2_NH['Visibility(mi)'] == 10.0]
    if data_severity_2_NH.empty:
        return "None"
    else:
        max_visibility = data_severity_2_NH['Visibility(mi)'].value_counts().idxmax()
        return max_visibility 

    #print(" ")
    #print("8. What was the maximum visibility of all accidents of severity 2 in new hampshire?")
    #print("The following is a dataframe with all accidents with visibility 10")
    #print(data_max_visibility)

# 9. how many accidents of each severity were recorded in bakersfield?
def Question9(data):


    #Filter data to only the city of Bakersfield
    data_Bakersfield = data[(data['City'] == 'Bakersfield')]
    if data_Bakersfield.empty:
        return "None"
    else:

        severity = data_Bakersfield['Severity'].value_counts().index.tolist()
        num_accidents = data_Bakersfield['Severity'].value_counts().values.tolist()

        result = str(num_accidents[0]) + " accidents of severity " + str(severity[0]) + ", " + str(num_accidents[1]) \
        + " accidents of severity " + str(severity[1]) + ", and " \
        + str(num_accidents[2]) + " accidents of severity " + str(severity[2])
        return result

        #if num_accidents.empty:
            #return "None"
        #else:
            #return num_accidents


    #print(" ")
    #print("# 9. how many accidents of each severity were recorded in bakersfield?")
    #print("The number of accidents of each severity recorded in Bakersfield are as follows: ")
    #print(num_accidents.to_string())

# 10. what was the longeset accident (in hours) recorded in florida in spring (mar, apr, may) of 2020?
def Question10(data):

    # Adding two extra columns to the data to filter based on year and month
    data['year'] = pd.DatetimeIndex(data['Start_Time']).year
    data['month'] = pd.DatetimeIndex(data['Start_Time']).month

    data['Start_Time'] = pd.to_datetime(data['Start_Time'], errors='coerce')
    data['End_Time'] = pd.to_datetime(data['End_Time'], errors='coerce')

    data['Duration'] = (data['End_Time'] - data['Start_Time']).dt.total_seconds() / 60 / 60

    # Filter data with only the year 2020 and Florida
    data_florida = data[(data['year'] == 2020) & (data['State'] == 'FL')] 
    if data_florida.empty:
        return "None"
    else:
        # Further filtering with the spring months(mar,apr,may)
        data_florida_spring = data_florida[(data_florida['month'] == 3) | (data_florida['month'] == 4) | (data_florida['month'] == 5)]
        if data_florida_spring.empty:
            return "None"
        else:
            longest_accident = data_florida_spring['Duration'].max()
            return longest_accident

# Search functions
def searchLocation(data,state,city,zip):
    locData = data
    if state != "":
        locData = locData[locData["State"] == state]
    if city != "":
        locData = locData[locData["City"] == city]
    if zip != "":
        locData = locData[locData["Zipcode"] == zip]

    if locData.empty:
        return "0"
    else:
        return locData.shape[0]

def searchTime(data,year,month,day):
    timeData = data
    timeData['year'] = pd.DatetimeIndex(timeData['Start_Time']).year
    timeData['month'] = pd.DatetimeIndex(timeData['Start_Time']).month
    timeData['day'] = pd.DatetimeIndex(timeData['Start_Time']).day

    if year != "":
        year = int(year)
        timeData = timeData[timeData["year"] == year]
    if month != "":
        month = int(month)
        timeData = timeData[timeData["month"] == month]
    if day != "":
        day = int(day)
        timeData = timeData[timeData["day"] == day]

    if timeData.empty:
        return "0"
    else:
        return timeData.shape[0]

def searchConditions(data,mintemp,maxtemp,minvis,maxvis):
    conData = data
    
    if mintemp != "":
        mintemp = float(mintemp)
        conData = conData[conData["Temperature(F)"] >= mintemp]
    if maxtemp != "":
        maxtemp = float(maxtemp)
        conData = conData[conData["Temperature(F)"] <= maxtemp]
    if minvis != "":
        minvis = float(minvis)
        conData = conData[conData["Visibility(mi)"] >= minvis]
    if maxvis != "":
        maxvis = float(maxvis)
        conData = conData[conData["Visibility(mi)"] <= maxvis]
    
    if conData.empty:
        return "0"
    else:
        return conData.shape[0]


# Flags for error handling
data_loaded = False
data_processed = False

# using the while loop to print menu list  
while True:
    print(" ")
    print("MENU")  
    print("1. Load data")  
    print("2. Process data")  
    print("3. Print Answers")  
    print("4. Search Accidents (Use City, State, and Zip Code)") 
    print("5. Search Accidents (Year, Month and Day)")
    print("6. Search Accidents (Temperature Range and Visibility Range)") 
    print("7. Quit") 

    try:
        users_choice = int(input("\nEnter your Choice: "))
        print()
    except ValueError:
        print(" ")
        print("Enter a number from the menu please.")
        continue


    # 1. Load data
    if users_choice == 1:
        if data_loaded == True:
            print(" ")
            print("Data already loaded.")
        else:
            print()
            start = time.time()
            print("****************")
            print('[{}] Starting script...'.format(ctime()))
            # reads file
            data = loadData(file)
            print('[{}]'.format(ctime()),'Loading "{}"...'.format(file))
            print('[{}]'.format(ctime()),"Total Columns Read:",data.shape[1])
            print('[{}]'.format(ctime()),"Total Rows Read:",data.shape[0])
            print()
            end = time.time()
            print("Time to process is: %s seconds" % (time.time() - start))
            print("****************")
            data_loaded = True

    # 2. Process data
    elif users_choice == 2:
        if data_loaded == False:
            print(" ")
            print("Please first load the data.")
        elif data_processed == True:
            print(" ")
            print(" Data already processed.")
        else:
            start = time.time()
            print(" ")
            print("****************")
            print('[{}]'.format(ctime()),"Performing Data Clean Up...")
            data = processData(data)
            print('[{}]'.format(ctime()),"Total Rows Read after cleaning:", data.shape[0])
            print()
            end = time.time()
            print("Time to process is: %s seconds" % (time.time() - start))
            print("****************")
            data_processed = True

    # 3. Print Answers
    elif users_choice == 3:
        if data_loaded == False:
            print(" ")
            print("Please first load data.")
        elif data_processed == False:
            print(" ")
            print("Please process the data.")
        else:
            print(" ")
            print("Answering Questions")
            print("*******************")
            print('[{}]'.format(ctime()),"In what month were there more accidents reported?")
            print('[{}]'.format(ctime()),Question1(data))
            print('[{}]'.format(ctime()),"What is the state that had the most accidents in 2020?")
            print('[{}]'.format(ctime()),Question2(data))
            print('[{}]'.format(ctime()),"What is the state that had the most accidents of severity 2 in 2021?")
            print('[{}]'.format(ctime()),Question3(data))
            print('[{}]'.format(ctime()),"What severity is the most common in Virginia?")
            print('[{}]'.format(ctime()),Question4(data))
            print('[{}]'.format(ctime()),"What are the 5 cities that had the most accidents in 2019 in California?")
            print('[{}]'.format(ctime()),Question5(data))
            print('[{}]'.format(ctime()),"What was the average humidity and average temperature of all accidents of severity 4 that occurred in 2021?")
            print('[{}]'.format(ctime()),Question6(data))
            print('[{}]'.format(ctime()),"What are the 3 most common weather conditions (weather_conditions) when accidents occurred?")
            print('[{}]'.format(ctime()),Question7(data))
            print('[{}]'.format(ctime()),"What was the maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire?")
            print('[{}]'.format(ctime()),Question8(data))
            print('[{}]'.format(ctime()),"How many accidents of each severity were recorded in Bakersfield?")
            print('[{}]'.format(ctime()),Question9(data))
            print('[{}]'.format(ctime()),"What was the longest accident (in hours) recorded in Florida in the Spring (March, April, and May) of 2020?")
            print('[{}]'.format(ctime()),Question10(data))
    elif users_choice == 4:
        if data_loaded and data_processed:
            print("Search Accidents by Location")
            print("****************************")
            state = input("Enter a State name: ")
            city = input("Enter a City name: ")
            zip = input("Enter a ZIP code: ")
            print()
            start = time.time()
            print("There were {} accidents".format(searchLocation(data,state,city,zip)))
            end = time.time()
            print()
            print("Time to perform search is: %s seconds" % (time.time() - start))
            print()
        elif not data_loaded and not data_processed:
            print("Please load and process data first")
        elif not data_loaded:
            print("Please load data")
        elif data_loaded and not data_processed:
            print("Please process data first")

    elif users_choice == 5:
        if data_loaded and data_processed:
            print("Search Accidents by Time")
            print("************************")
            year = input("Enter a year: ")
            month = input("Enter a month: ")
            day = input("Enter a day: ")
            print()
            start = time.time()
            print("There were {} accident(s)".format(searchTime(data,year,month,day)))
            end = time.time()
            print()
            print("Time to perform search is: %s seconds" % (time.time() - start))
            print()
        elif not data_loaded and not data_processed:
            print("Please load and process data first")
        elif not data_loaded:
            print("Please load data")
        elif data_loaded and not data_processed:
            print("Please process data first")

    elif users_choice == 6:
        if data_loaded and data_processed:
            print("Search Accidents by Condition")
            print("*****************************")
            minTemp = input("Enter a minimum temperature(F): ")
            maxTemp = input("Enter a maximum temperature(F): ")
            minVis = input("Enter a minimum visibility(mi): ")
            maxVis = input("Enter a maximum visibility(mi): ")
            print()
            start = time.time()
            print("There were {} accident(s)".format(searchConditions(data,minTemp,maxTemp,minVis,maxVis)))
            end = time.time()
            print()
            print("Time to perform search is: %s seconds" % (time.time() - start))
            print()
        elif not data_loaded and not data_processed:
            print("Please load and process data first")
        elif not data_loaded:
            print("Please load data")
        elif data_loaded and not data_processed:
            print("Please process data first")

    elif users_choice == 7:
        endofcode = timer()
        print("Total Running Time: %s Minutes" % ((endofcode - startofcode)/60))
        break

    else:
        print(" ")
        print("Please enter a valid Input from the menu.")

#print(data)
