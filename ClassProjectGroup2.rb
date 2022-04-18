# Course: CMPS 3500
# Class Project
# Ruby Implementation: Basic Data Analysis
# Date: 4/12/2022
# Student 1: Patrick Park
# Student 2: Carlos Hernandez
# Student 3: Edmund Felicidario
# Student 4: Juan Sierra Diaz

#!/usr/bin/env ruby
require 'daru'
require 'csv'



df = Daru::DataFrame.from_csv('test_data.csv')
puts df