# Course: CMPS 3500
# Class Project
# Python Implementation: Basic Data Analysis
# Date: 4/12/2022
# Student 1: Patrick Park
# Student 2: Carlos Hernandez
# Student 3: Edmund Felicidario
# Student 4: Juan Sierra Diaz

# imports pandas, a useful data science library
import pandas as pd

# reads file
data = pd.read_csv("test_data.csv", index_col=0)

# removes rows with specific missing data
validData = data.dropna(subset=['ID', 'Severity', 'Zipcode','Start_Time','End_Time','Visibility(mi)', 'Weather_Condition','Country'])

# resets index numbers
validData.reset_index(drop=True,inplace=True)

# prints all rows after cleanup
print(validData)
