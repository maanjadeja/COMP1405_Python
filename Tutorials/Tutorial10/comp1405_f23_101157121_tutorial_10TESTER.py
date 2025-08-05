#Name: Maansinh Jadeja
#Student Number: 101157121

import random


def checkForSort(givenList):

    listInOrder=False
    for i in range(0,len(givenList)-1):
        if(givenList[i]<=givenList[i+1]): #Check if current element is less than or equal to the next element
            listInOrder=True
        else:
            listInOrder=False
            break
    
    return listInOrder

def bogoSort(givenList):

    originalList = givenList[:]
    newList=[]
    for j in range(0, len(originalList)):
        randomIndex=random.randint(0,len(originalList)-1) #Select a random index within the index boundaries of the array
        value=originalList.pop(randomIndex) #use the pop() function to remove the element and place the value into newList
        newList.append(value)

    print(newList)
    
    return checkForSort(newList)

def bozoSort(givenList):

    originalList = givenList[:]

    newList=givenList

    for j in range(0, len(newList)-1):
        firstRandomIndex = random.randint(0,len(originalList)-1) #Select random values within the index boundaries of the array to swap
        secondRandomIndex = random.randint(0,len(originalList)-1)
        if(firstRandomIndex==secondRandomIndex): #Make sure the random values do not match
            secondRandomIndex = random.randint(0,len(originalList)-1)
            firstThing = newList[firstRandomIndex] #Swap the values
            newList[firstRandomIndex] = newList[secondRandomIndex]
            newList[secondRandomIndex] = firstThing

            
    #     print(f"first {firstRandomIndex}")
    #     print(f"second {secondRandomIndex}")
    
    print(newList)

    return checkForSort(newList)

def main():

    listOfNum=[]

    for i in range(0,5): #Fill an array with random 5 values within range of 0-10
        randomValue=random.randint(0,10)
        listOfNum.append(randomValue)
    
    #To test both functions comment the other to test 1 at a time

    #BOGO SORT COMPLETE
    print(listOfNum)
    # goodList=[3,2,1]
    print("BOGO SORT")
    print(bogoSort(listOfNum)) #Run Bogo Sort
    while(bogoSort(listOfNum)==False):
        print(bogoSort(listOfNum))
    

    
    # print(bozoSort(goodList))
    #BOZOSORT COMPLETE
    # print("BOZO SORT")
    # print(bozoSort(listOfNum)) #Run Bozo Sort
    # while(bozoSort(listOfNum)==False):
    #     print(bozoSort(listOfNum))

main()


