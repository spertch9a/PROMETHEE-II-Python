"""
Authon Oussama FORTAS
"""
import numpy as np
print("PROMETHEE 2 METHOD")
print("#######################################################")

print("We will be using AHP : Analytic Hierarchy Process.")

#We'll use the mobile choosing example, 
"""
The criterias to choose upon are 
(Weightage= 0.35) Price or Cost 
(Weightage=0.25 ) Storage space
(Weightage=0.25 ) Camera
(Weightage=0.15 ) Looks =  {Excellent : 5 , Good : 4 , Average : 3  , Below Average :2 , Low : 1}
"""


Matrix = [["Attribute or Criteria", "Price or Cost", "Storage Space", "Camera", "Looks"], 
    ["Mobile 1", 250, 16, 12, 5],
    ["Mobile 2", 200, 16, 8 ,3],
    ["Mobile 3", 300, 32, 16, 4],
    ["Mobile 4", 275, 32, 8, 2]]

#to print matrix in a good format 
#len(matix) gives us the number of rows
def printmatrix (matrix): 
    for i in range(len(matrix)) :  
        for j in range(len(matrix[i])) :  
            print(matrix[i][j], end=" ") 
        print() 

printmatrix(Matrix)

print("Full Ranking")

#Step 1 : Normalize the Evaluation Matrix (decision matrix) 
print("STEP 1 : Normalize the Evaluation Matrix")
"""
Captures / Formula for beneficial and non beneficial criteria
Beneficial are direct categories
Non beneficial are indirect ones
For each criteria we need to calculate the maximum and minimum for each criteria
"""
npmatrix  = np.array(Matrix)
subnpmatix = npmatrix[1:,1:]
print("npmatrix ")

maxprice= 0  
maxstorage= 0
maxcamera = 0
maxlooks= 0 
minprice = 1000
minstorage = 1000
mincamera = 1000
minlooks = 1000
y = subnpmatix.astype(np.float)
def maxminprice(matrix) :
    maxprice = 0
    minprice  = 1000
    for row in range(len(matrix)):
     if(maxprice < matrix[row][0]) : 
        maxprice = matrix[row][0]
     if(minprice > matrix[row][0]) :     
        minprice = matrix[row][0]

    return maxprice, minprice
def maxminstorage(matrix) :
    maxstorage = 0
    minstorage  = 1000
    for row in range(len(matrix)):
     if(maxstorage < matrix[row][1]) : 
        maxstorage = matrix[row][1]
     if(minstorage > matrix[row][1]) :     
        minstorage = matrix[row][1]

    return maxstorage, minstorage

def maxmincamera(matrix) :
    maxcamera = 0
    mincamera  = 1000
    for row in range(len(matrix)):
     if(maxcamera < matrix[row][2]) : 
        maxcamera = matrix[row][2]
     if(mincamera > matrix[row][2]) :     
        mincamera = matrix[row][2]

    return maxcamera, mincamera

def maxminlooks(matrix) :
    maxlooks = 0
    minlooks  = 1000
    for row in range(len(matrix)):
     if(maxlooks < matrix[row][3]) : 
        maxlooks = matrix[row][3]
     if(minlooks > matrix[row][3]) :     
        minlooks = matrix[row][3]

    return maxlooks, minlooks



print("maxminprice : ", maxminprice(y))
print("maxminstorage : ", maxminstorage(y))
print("maxmincamera : ", maxmincamera(y))
print("maxminlooks : ", maxminlooks(y))

#STEP 2 :  calcule des difference 
def calculeDiff():
    #max_col  - min_c


# https://www.youtube.com/watch?v=xe2XgGrI0Sg&t=55s









