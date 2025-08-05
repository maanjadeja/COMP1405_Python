#Name: Maansinh Jadeja
#Student Number: 101157121 
#Assignment 6
import random

#1st function: interact with user and result in the creation of a list of integers to be returned by the function
def createList():

    userResponse=""

    numList = []
    x = random.randint(1,10)
    numList.append(x)
    print(numList)

    while(userResponse.upper()!="NO"):
        userResponse=input("Would you like to continue adding elements to the list? YES/NO: ")
        x = random.randint(1,10)
        numList.append(x)
        print(numList)
    
    return numList


    # print(x)


#2nd function: implementation of missing component (for which u created flowchart) and will accept list of integers returned from
#the 1st function as an argument and will return the modified list of integers (list after having some elements removed)
def modifyList(inputList):

    userResponse=""

    if(len(inputList)>6):
        inputList.pop(6)

    while(userResponse.upper()!="NO"):
        userResponse= input("Would you like to continue removing value at index 6? YES/NO: ")
        if(len(inputList)>6):
            inputList.pop(6)
            print(inputList)
        else:
            print(inputList)
            break

    return inputList    
    


#3rd function: implement everything after the missing component up to (but not including) printing the final result to the terminal
#3rd function: will accept the list of integers returned by the 2nd function as an argument and will process the elements of ur
#initial list into a new list, then it will return that new list to be printed out in your main() function
#THIS IS A PLACEHOLDER FUNCTION, meaning it must accept the argument list of integers and return that same list of integers 
#*UNMODIFIED*

def createNewList(initialList):
    newList=[]
    
    i=0
    while(i<len(initialList)):
        if(initialList[i]>3):
            print(initialList)
            newList.append(initialList[i])
            print(newList)
   
        i+=1
    
    print(newList)
    return newList
        


def main():
    currList=createList()
    print(f"THE LIST: {currList}")
    currList1=modifyList(currList)
    print(f"THE MODIFIED LIST: {currList1}")
    currList2=createNewList(currList1)
    print(f"THE FINAL MODIFIED LIST: {currList2}")


main()
