import csv
import numpy as np

with open('MP.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
 matrix = np.array(csv_reader)  
 print( "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")     
 print(matrix)