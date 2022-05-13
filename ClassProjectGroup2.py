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
file = "US_Accidents_data.csv"

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

    # Convert the month number to the full month name
    full_month_name = datetime_object.strftime("%B")

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
 

# 3. what state had most accidents with severity 2 in 2021?
def Question3(data):

    # Add and extra column with only the year
    data['year'] = pd.DatetimeIndex(data['Start_Time']).year

    # Filter data with year 2021 and only states with Severity == 2
    data_2021 = data[(data['year'] == 2021) & (data['Severity'] == 2)]
    if data_2021.empty:
        return "None"
    else:
        # Get the state with most accidents with severity 2.
        states_severity_2 = data_2021['State'].value_counts().idxmax()
        return states_severity_2


# 4. what severity is most common in Virginia?
def Question4(data):
    
    # Filter data with only the state of Virginia
    data_virginia = data[(data['State'] == 'VA')]

    if data_virginia.empty:
        return "None"
    else:
        # Get the most common severity
        most_common_severity = data_virginia['Severity'].value_counts().idxmax()
        return most_common_severity


#5. what are the 5 cities that had the most accidents in 2019 in CA?
def Question5(data):

    # Add extra coloumn with only the year
    data['year'] = pd.DatetimeIndex(data['Start_Time']).year

    # Filter data with the year 2019 and state CA only
    data_2019_CA = data[(data['year'] == 2019) & (data['State'] == 'CA')]

    if data_2019_CA.empty:
        return "None"
    else:
        # Get the top 5 cities from filtered data
        top_five_cities = data_2019_CA['City'].value_counts().index.tolist()[:5]

        # For print purposes, the answer was formatted this way. 
        result = top_five_cities[0] + ", " + top_five_cities[1] + ", " + top_five_cities[2] + ", " + top_five_cities[3] + ", " + top_five_cities[4]

        return result

#6. what was the avg humidity and avg temp of all accidents of severity 4 in 2021?
def Question6(data):

    # Add extra column with only the year
    data['year'] = pd.DatetimeIndex(data['Start_Time']).year

     # Filter data with only the year 2021 and Severity 4
    data_2021_Severity_4 = data[(data['year'] == 2021) & (data['Severity'] == 4)]

    if data_2021_Severity_4.empty:
        return "None"
    else:

        # Get the total sum of Humidity and Temperature
        humidity_sum = data_2021_Severity_4['Humidity(%)'].sum()
        temperature_sum = data_2021_Severity_4['Temperature(F)'].sum()
        
        # Get lenght, number of items in that coloumn
        length_humidity = len(data_2021_Severity_4['Humidity(%)'])
        length_tem = len(data_2021_Severity_4['Temperature(F)'])

        #Calculate averages
        humidity_ave = humidity_sum/length_humidity
        temperature_ave = temperature_sum/length_tem

        # Formating the output
        result = "Average Humidity: " + str(round(humidity_ave,2)) + "%, " + "Average Temperature: " + str(round(temperature_ave,2)) + " F"

        return result


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
        
        # Formating for output purposes
        result = three_common_weather_conditions[0] + ", " + three_common_weather_conditions[1] + ", " + three_common_weather_conditions[2]

        return result


# 8. what was the maximum visibility of all accidents of severity 2 in new hampshire?
def Question8(data):

    # Filter data with accidents of New Hampshire with severity 2 
    data_severity_2_NH = data[(data['Severity'] == 2) & (data['State'] == 'NH')]

    #data_max_visibility = data_severity_2_NH[data_severity_2_NH['Visibility(mi)'] == 10.0]
    if data_severity_2_NH.empty:
        return "None"
    else:
        # Get the maximun visibility
        max_visibility = data_severity_2_NH['Visibility(mi)'].value_counts().idxmax()
        return max_visibility 

# 9. how many accidents of each severity were recorded in bakersfield?
def Question9(data):

    #Filter data to only the city of Bakersfield
    data_Bakersfield = data[(data['City'] == 'Bakersfield')]

    if data_Bakersfield.empty:
        return "None"
    else:

        # Getting Severities, and storing them is a list
        severity = data_Bakersfield['Severity'].value_counts().index.tolist()

        # Getting number of accidents of each individual severity and storing them in a a list
        num_accidents = data_Bakersfield['Severity'].value_counts().values.tolist()

        # Formatting each severity with its respective number of accidents
        result = str(num_accidents[0]) + " accidents of severity " + str(severity[0]) + ", " + str(num_accidents[1]) \
        + " accidents of severity " + str(severity[1]) + ", and " \
        + str(num_accidents[2]) + " accidents of severity " + str(severity[2])

        if not num_accidents and not severity:
            return "None"
        else:
            return result


# 10. what was the longeset accident (in hours) recorded in florida in spring (mar, apr, may) of 2020?
def Question10(data):

    # Adding two extra columns to the data to filter based on year and month
    data['year'] = pd.DatetimeIndex(data['Start_Time']).year
    data['month'] = pd.DatetimeIndex(data['Start_Time']).month

    # Isolating only the time, this was necessary as 'Start_Time' and 'End_Time'
    # also contain the full date
    data['Start_Time'] = pd.to_datetime(data['Start_Time'], errors='coerce')
    data['End_Time'] = pd.to_datetime(data['End_Time'], errors='coerce')

    # Coverting duration to hours
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
            # Get the longest accident in hours
            longest_accident = data_florida_spring['Duration'].max()
            return longest_accident

# list of states and months and their abbreviations
states = ["ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", "CONNECTICUT", "DELAWARE", "FLORIDA", "GEORGIA", "HAWAII", "IDAHO", "ILLINOIS", "INDIANA", "IOWA", "KANSAS", "KENTUCKY", "LOUISIANA", "MAINE", "MARYLAND", "MASSACHUSETTS", "MICHIGAN", "MINNESOTA", "MISSISSIPPI", "MISSOURI", "MONTANA", "NEBRASKA", "NEVADA", "NEW HAMPSHIRE", "NEW JERSEY", "NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA", "OHIO", "OKLAHOMA", "OREGON", "PENNSYLVANIA", "RHODE ISLAND", "SOUTH CAROLINA", "SOUTH DAKOTA", "TENNESSEE", "TEXAS", "UTAH", "VERMONT", "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING"]
abbrev = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
abbrevMonths = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

# helper & validation functions
# checks if state input is an actual state (full state name or abbrev)
def validateState(state):
    cleanState = state.upper()
    if cleanState in states or state in abbrev:
        return True
    else:
        return False

# formats the state input and returns the abbreviated name
def stateHelper(state):
    cleanState = state.upper()
    if state == "":
        return state
    elif cleanState in states:
        return abbrev[states.index(cleanState)]
    else:
        return abbrev[abbrev.index(cleanState)]

# checks if zip code contains only digits and a length of 5 characters
def validateZip(zip):
    if zip.isdigit() and len(zip) == 5:
        return True
    else:
        return False

# validates if year is > 0
def validateYear(year):
    if year.isdigit() and int(year) >= 0 or year == "":
        return True
    else:
        return False

# checks if the month input is valid
def validateMonth(month):
    if month.isdigit() and int(month) >= 1 and int(month) <= 12 or month == "":
        return True
    elif month.isalpha():
        cleanMonth = month.upper()
        if cleanMonth in months:
            return True
        elif cleanMonth in abbrevMonths:
            return True
        else:
            return False
    else:
        return False

# formats the month input and returns the month number
def monthHelper(month):
    cleanMonth = month.upper()
    if month == "":
        return month
    elif cleanMonth == "SEPT":
        return "9"
    elif cleanMonth in months:
        return str(months.index(cleanMonth)+1)
    elif cleanMonth in abbrevMonths:
        return str(abbrevMonths.index(cleanMonth)+1)
    else:
        return month

# validates if input is a valid day of the month (1-31)
def validateDay(day):
    if year.isdigit() and int(day) >= 1 and int(day) <= 31 or day == "":
        return True
    else:
        return False

# generic number validation for humidity and temperature
def validateNum(num):
    if num.isdigit():
        return True
    else:
        return False

# Search functions
# search accidents by specifying location 
def searchLocation(data,state,city,zip):
    state = state.upper()
    city = city.capitalize()
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

# search accidents by specifying date
def searchDate(data,year,month,day):
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

# search accidents by specifying weather 
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
            print('[{}]'.format(ctime()),round(Question10(data),4))
    elif users_choice == 4:
        if data_loaded and data_processed:
            print("Search Accidents by Location")
            print("****************************")
            state = input("Enter a State name or initials: ")
            while validateState(state) == False and state != "":
                print("Invalid State. Please try again.")
                state = input("Enter a State name or initials: ")
            city = input("Enter a City name: ")
            zip = input("Enter a 5-digit ZIP code: ")
            while validateZip(zip) == False and zip != "":
                print("Invalid Zip code. Please try again.")
                zip = input("Enter a 5-digit ZIP code: ")
            print()
            start = time.time()
            print("There were {} accidents".format(searchLocation(data,stateHelper(state),city,zip)))
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
            print("Search Accidents by Date")
            print("************************")
            year = input("Enter a year: ")
            while validateYear(year) == False and year != "":
                print("Invalid year. Please try again.")
                year = input("Enter a year: ")
            month = input("Enter a month: ")
            while validateMonth(month) == False and month != "":
                print("Invalid month. Please try again.")
                month = input("Enter a month: ")
            day = input("Enter a day: ")
            while validateDay(day) == False and day != "":
                print("Invalid day. Please try again.")
                day = input("Enter a day: ")
            print()
            start = time.time()
            print("There were {} accident(s)".format(searchDate(data,year,monthHelper(month),day)))
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
            while validateNum(minTemp) == False and minTemp != "":
                print("Invalid value. Please try again.")
                minTemp = input("Enter a minimum temperature(F): ")
            maxTemp = input("Enter a maximum temperature(F): ")
            while validateNum(maxTemp) == False and maxTemp != "":
                print("Invalid value. Please try again.")
                maxTemp = input("Enter a maximum temperature(F): ")
            minVis = input("Enter a minimum visibility(mi): ")
            while validateNum(minVis) == False and minVis != "":
                print("Invalid value. Please try again.")
                minVis = input("Enter a minimum visibility(mi): ")
            maxVis = input("Enter a maximum visibility(mi): ")
            while validateNum(maxVis) == False and maxVis != "":
                print("Invalid value. Please try again.")
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