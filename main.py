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

maxprice, minprice = maxminprice(y)
maxstorage, minstorage = maxminstorage(y)
maxcamera, mincamera = maxminstorage(y)
maxlooks, minlooks = maxminlooks(y)
#STEP 2s,m :  calcule des difference
#max_col  - courant_col / max_col - min_col 
subnpmatixmaxed = np.vstack([subnpmatix, [maxprice, maxstorage, maxcamera, maxlooks]])
subnpmatixmaxedminimizeded = np.vstack([subnpmatixmaxed, [minprice, minstorage, mincamera, minlooks]])
#hna la matrice ta3na ghedi nwejedhalkom bach nakharbo fiha 
y = subnpmatixmaxedminimizeded.astype(np.float)
print(subnpmatixmaxedminimizeded)
print(y)





def calculeDiffbeneficial(value, max_colmn,min_colmn):
    return ((value - min_colmn) / (max_colmn - min_colmn))
    
def calculedifferencenonbeneficial(value,max_colmn, min_colmn):
    return ((max_colmn - value) / (max_colmn - min_colmn))



print(calculeDiffbeneficial(16,18,4))

def steptwo(entrymatrix) :
    for i in range(len(entrymatrix-2)) :  
    #hna reni f  ligne
        for j in range(len(entrymatrix[i])) :  
            #hna reni f la column
            if j == 0: 
                entrymatrix[i][j] = calculedifferencenonbeneficial(entrymatrix[i][j],entrymatrix[4][j], entrymatrix[5][j])
            else :
                entrymatrix[i][j] = calculeDiffbeneficial(entrymatrix[i][j],entrymatrix[4][j], entrymatrix[5][j])
           
    #hna reni rod la matrice m3Amra
    return entrymatrix            

#gla3T zouj stoura twala
matrixaftersteptwo = steptwo(y)[:4][:4]
 
 #darwek li raha taht 0 nrodha 0 
def changetozeros(matrix):
    for i in range(len(matrix)) :  
        for j in range(len(matrix[i])) :  
           if matrix[i][j] <0 :
                matrix[i][j] = 0
    return matrix 

matrixafterchange = changetozeros(matrixaftersteptwo)
#STEP3 : nahasbou koul wahda w difference m3A lokhrine

names = ['price', 'storage', 'camera', 'looks']
starm1m2 = []
matrix_m1 = matrixafterchange
matrix_m2 = matrixafterchange
matrix_m3 = matrixafterchange
matrix_m4 = matrixafterchange

matrixX, matrixY = matrix_m1.shape

def stepthree(matrix, ligne) :
	print('Alternative : {}'.format(ligne))
	if (ligne != 1):
		matrix[[0,ligne-1]] = matrix[[ligne-1, 0]]
	else:
		pass

	new_matrix = []
	reverse_matrix = matrix.transpose()
	
	for line in reverse_matrix:
		data = []
		for i in line[1:]:
			data.append(line[0]-i)
		new_matrix.append(data)
	
	result_matrix = np.matrix(new_matrix).transpose()

	print(result_matrix)



stepthree(matrix_m1, 1)
stepthree(matrix_m2, 2)
stepthree(matrix_m3, 3)
stepthree(matrix_m4, 4)



