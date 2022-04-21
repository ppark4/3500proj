# Course: CMPS 3500
# Class Project
# Ruby Implementation: Basic Data Analysis
# Date: 4/12/2022
# Student 1: Patrick Park
# Student 2: Carlos Hernandez
# Student 3: Edmund Felicidario
# Student 4: Juan Sierra Diaz

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
# data cleaning:
# 1. load csv file and store in array/dataframe
# 2. eliminate rows with missing data in..(see prompt)
# 3. eliminate rows with empty values in 3 or more columns
# 4. eliminate rows with distance zero 
# 5. only consider in your analysis the first 5 digits of the zip
# 6. eliminate? rows that lasted no time (endtime - starttime = 0)
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

#!/usr/bin/env ruby
require 'daru'
require 'csv'



df = Daru::DataFrame.from_csv('test_data.csv')
puts df