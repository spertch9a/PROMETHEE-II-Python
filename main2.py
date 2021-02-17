"""
Author Oussama FORTAS
"""
print("PROMETHEE 2 METHOD")
print("#######################################################")

print("We will be using AHP : Analytic Hierarchy Process.")

import csv
import numpy as np

Matrix = np.array(list(csv.reader(open("MP.csv", "r", encoding="utf8"), delimiter=",")))
print(Matrix)
#to print matrix in a good format 
#len(matix) gives us the number of rows


# Step1 Normalize the evaluation matrix (Decision Matrix)
print("STEP 1 : Normalize the Evaluation Matrix")
# make the matrix as array to facilitate the Loop function
array_Matrix  = np.array(Matrix)
# Delete first ligne and column and keep only the float variables
Alternative_matix = array_Matrix[1:,1:].astype(np.float)
print(Alternative_matix)
# Get min and max for each criteria
min_criteria_array = Alternative_matix.min(axis=0)
max_criteria_array = Alternative_matix.max(axis=0)
print(min_criteria_array)
print(max_criteria_array)

# Calculate the new matrix with beneficial non beneficial criteria:
# Beneficial Criteria == 1
# NON ben Criteria == 2,3,4
for i in range(len(Alternative_matix)):
    for j in range(len(Alternative_matix[i])):
        if j == 1:
            Alternative_matix[i][j] = (max_criteria_array[j]-Alternative_matix[i][j])/(max_criteria_array[j]-min_criteria_array[j])
        else:
            Alternative_matix[i][j] = (max_criteria_array[j]-Alternative_matix[i][j])/(max_criteria_array[j]-min_criteria_array[j])