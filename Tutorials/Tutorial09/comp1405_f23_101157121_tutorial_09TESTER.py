#Name: Maansinh Jadeja
#Student Number: 101157121

import sys
import random

def addMatrices(matrix1, matrix2):
    finalMatrix=[]

    if(len(matrix1)!=len(matrix2)):
        print("ERROR: DIFFERENT LENGTHS")
    else:
        if(len(matrix1[0])!=len(matrix2[0])):
            print("ERROR: DIFFERENT NUMBER OF VALUES PER ROW")
        else:
            for i in range(0, len(matrix1)):
                rowSum=[]
                for j in range(0, len(matrix1[0])):
                    # print(f"MATRIX1: {matrix1[i][j]}")
                    # print(f"MATRIX2: {matrix2[i][j]}")
                    sumValue = matrix1[i][j]+matrix2[i][j]
                    rowSum.append(sumValue)
                    
                    # rowSum.append(matrix1[i][j]+matrix2[i][j])
            
                finalMatrix.append(rowSum)
    
    print(f"FINAL MATRIX: {finalMatrix}")

    return finalMatrix

            

def main():

    matrixList1 = []
    matrixList2 = []

    userResponse1R = input("How many rows in Matrix 1: ")
    userResponse1V = input("How many values per row in Matrix 1: ")

    if(userResponse1R.isnumeric() and userResponse1V.isnumeric()):
        for i in range(0,int(userResponse1R)): #num of rows
            newList=[]
            for j in range(0,int(userResponse1V)):
                randomValue = random.randint(0,10)
                newList.append(randomValue)

            matrixList1.append(newList)
    
    # print(matrixList1)
    print(f"MATRIX LIST 1: {matrixList1}")


    userResponse2R = input("How many rows in Matrix 2: ")
    userResponse2V = input("How many values per row in Matrix 2: ")

    if(userResponse2R.isnumeric() and userResponse2V.isnumeric()):
        for i in range(0,int(userResponse2R)): #num of rows
            newList=[]
            for j in range(0,int(userResponse2V)):
                randomValue = random.randint(0,10)
                newList.append(randomValue)

            matrixList2.append(newList)
    print(f"MATRIX LIST 2: {matrixList2}")

    if(len(matrixList1)>0 and len(matrixList2)>0):
        addMatrices(matrixList1, matrixList2)


main()


