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

def maxminmatrix(matrix) :
    maxprice = 0
    minprice  = 0
    for row in range(len(matrix)):
     if(int(maxprice) < int(matrix[row][0])) : 
        maxprice = matrix[row][0]
     if(minprice > matrix[row][0]) :     
        minprice= matrix[row][0]
    return maxprice


print("maxprice : ", maxminmatrix(subnpmatix))