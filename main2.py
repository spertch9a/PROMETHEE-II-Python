"""
Authors Oussama FORTAS
        Aimene BAHRI
        Ali Atmani
        Abed Kebir
"""
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
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
print('Alternative_matix \n',Alternative_matix)
# Save the Labels of the Ligne we deleted (we will need it later)
labels = array_Matrix[0,1:]
print('labels \n',labels)
# Save the Names of the Column we deleted (we will need it later)
Alternatives = array_Matrix[1:,0]
print('Names \n',Alternatives)
# Get min and max for each criteria
min_criteria_array = Alternative_matix.min(axis=0)
max_criteria_array = Alternative_matix.max(axis=0)
print(min_criteria_array)
print(max_criteria_array)

# Calculate the new matrix with beneficial non beneficial criteria:
# Beneficial Criteria == 1(python nebdou mel 0)
# NON ben Criteria == 2,3,4(python == 1,2,3)
for i in range(len(Alternative_matix)):
    for j in range(len(Alternative_matix[i])):
        if j == 0:
            Alternative_matix[i][j] = (max_criteria_array[j]-Alternative_matix[i][j])/(max_criteria_array[j]-min_criteria_array[j])
        else:
            Alternative_matix[i][j] = (Alternative_matix[i][j]-min_criteria_array[j])/(max_criteria_array[j]-min_criteria_array[j])

print(Alternative_matix)

print("STEP 2 : Calculate Evaluative ieme per the othere {m1-m2 | m1-m3 | ....}")
# Create the Alternatives Possibilities array[m1-m2,........]
def all_alternatives(Alternatives):
    Alternative_possibilities = []
    for i in range(len(Alternatives)):
        for j in range(len(Alternatives)):
            if i != j:
                Alternative_possibilities.append(Alternatives[i]+'-'+Alternatives[j])
            else:
                pass
    return np.array(Alternative_possibilities).reshape(len(Alternative_possibilities),1)
Alternative_possibilities = all_alternatives(Alternatives)
print('Alternative_possibilities \n', Alternative_possibilities)

# create the matrix of all variables possibilities:
def all_variables(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j:
                new_matrix.append(matrix[i]-matrix[j])
            else:
                pass
    return np.array(new_matrix).reshape(len(matrix)*(len(matrix)-1),len(matrix))

variables_possibilities = all_variables(Alternative_matix)
print('variables_possibilities \n', variables_possibilities)

# concatenate the Names and variables related 
the_all_matrix = np.hstack([Alternative_possibilities, variables_possibilities])
print('The All Matrix \n', the_all_matrix)

print("STEP 3 : Calculate the PREFERENCE Function")
# Create an updated matrix that return 0 if value is negative or equal to 0 
# else keep value as it it
def changetozeros(matrix):
    for i in range(len(matrix)) :  
        for j in range(len(matrix[i])) :  
            if matrix[i][j] <= 0 :
                matrix[i][j] = 0
    return matrix

Preference_matrix = changetozeros(variables_possibilities)
print('PREFERENCE_matrix \n', Preference_matrix)

# concatenate the Names and preferences related 
the_Preference_matrix = np.hstack([Alternative_possibilities, Preference_matrix])
print('the_Preference_matrix \n', the_Preference_matrix)

# calculate the aggregated preferenbce function
# hna nedourbou f les poids(weights)
# lets call the weights from a csv file
weights =list(csv.reader(open("weights.csv", "r", encoding="utf8"), delimiter=","))
print('weights \n', weights)
array_weights = np.asarray(weights[0], dtype='float64')
print('array_weights \n', array_weights)

# lets create a fucntion to mult the weights with the matrix of preferences variables
def mult_matrix_vect(matrix, weight):
    for i in range(len(matrix)) :  
        for j in range(len(matrix[i])) :  
            matrix[i][j] = matrix[i][j]* weight[j]
    return matrix
# TODO: Check this multyplie function
def show_mult_matrix_vect(matrix, weight):
    data = []
    for i in range(len(matrix)) :  
        print(range(len(matrix)))
        for j in range(len(matrix[i])) : 
            print(range(len(matrix[i]))) 
            data.append('{}*{}'.format(weight[j],matrix[i][j]))
    return np.array(data)

Agregate_preference_matrix = mult_matrix_vect(Preference_matrix, array_weights)
show_calculation = show_mult_matrix_vect(Preference_matrix, array_weights)

print('show_calculation \n', show_calculation)
print('Agregate_preference_matrix \n', Agregate_preference_matrix)

# lets add a column to sum these aggregated preferences
def add_aggregated_preferences_line(matrix):
    average_line_weight = []
    
    for i in range(len(matrix)) :
        sum = 0  
        for j in range(len(matrix[i])) :
            sum = sum + matrix[i][j] 
        average_line_weight.append(sum)
        
    matrix = np.vstack([matrix.transpose(), average_line_weight]).transpose()
    return matrix

Agregate_preference_matrix_with_sum = add_aggregated_preferences_line(Agregate_preference_matrix)
print('Agregate_preference_matrix_with_sum \n', Agregate_preference_matrix_with_sum)
aggrsums = Agregate_preference_matrix_with_sum[:,-1]
print(aggrsums)
# take only the aggragated sum values(LAST column) and create aggregated preference Function
def create_aggregated_matrix(matrix, aggr):
    # retrieve only the aggregated column(list)
    aggregate_column = np.array(matrix[:, -1].transpose())
    agrs = aggr.tolist()
    print(aggregate_column)
    print("type of aggregate_column")
    print(type(aggregate_column))
  #  aggregated_matrix  = [[len(Alternatives), len(Alternatives) ]]
    #hada el hmar ghadi ylez madam les valeurs yethattou
   # print(np.array(aggregated_matrix).shape)
    for i in range(len(aggregated_matrix)) :  
        for j in range(len(aggregated_matrix[i])) : 
            print(i,j)
            
            if i == j:
                aggregated_matrix[i][j] = 0        
            else:  
                aggregated_matrix[i][j]= agrs[0]
                agrs.pop(0) 
            
                
                # aggregated_matrix.append(aggregate_column[j])
    # print('lol',aggregated_matrix)
    print(np.array(aggregated_matrix).shape)
    return aggregated_matrix
    
aggregated_matrix = np.zeros((len(Alternatives), len(Alternatives)))

print("len alternatives")
print(len(Alternatives))
hamoud = create_aggregated_matrix(aggregated_matrix, aggrsums)

print("HADA HAMOUD")
print(hamoud)
linesha9eh = hamoud
#flot entrant w sortant
def sumColumn(m):
    return [sum(col) for col in zip(*m)] 

sommeeecolonne= sumColumn(hamoud)

sumrows = np.sum(hamoud, axis = 1)
#we need to deivde those calculated vvalues on the number of alternatives -1
newsommecolonne = []
newsumrow= []
for x in sommeeecolonne:
    newsommecolonne.append(x /(len(hamoud) - 1))

for x in sumrows:
    newsumrow.append(x /(len(hamoud) - 1))


print(sommeeecolonne)
print(sumrows)        
print("flots entrants \n" , newsommecolonne)
print("flots sortants \n" , newsumrow)

hamoud = np.vstack([hamoud, newsumrow])
print("b colmns ")
print(hamoud)

newsommecolonne.append(0)
hamoud= np.vstack([hamoud.transpose(), newsommecolonne]).transpose()
print("hamoud kamel\n", hamoud)


#here i'll be using a function to calculate the flots 
def calculateflows(matrix):
    diffs=[]
    for i in range(len(matrix)):
        diffs.append(matrix[i,-1] - matrix[-1, i])
    return diffs

print("flowshamoud")
differencesflots = calculateflows(hamoud)
print(differencesflots)


alt = np.append(Alternatives, " ")
linesha9eh = np.vstack([alt, hamoud.transpose()])
#so far hamoud is transposed 


# def remove_last_element(arr):
#     return arr[np.arange(arr.size - 1)]
# fachnhat = remove_last_element(fachnhat)

talyabachtetsetef  = np.vstack([linesha9eh, differencesflots]).transpose()
print("sma3")
print("##############")
print(talyabachtetsetef)

# Sort 2D numpy array by first column
sortedArr = talyabachtetsetef[talyabachtetsetef[:,-1].argsort()]
print('Sorted 2D Numpy Array')
print("##############")
print(np.flipud(sortedArr))
print("Final Sort is : ")
print(sortedArr[:,0])