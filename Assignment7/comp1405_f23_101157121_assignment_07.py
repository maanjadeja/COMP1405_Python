#Name: Maansinh Jadeja
#Student Number: 101157121 
#Assignment 7
import random

#1st function: interact with user and result in the creation of a list of integers to be returned by the function
def createList():

    userResponse=""

    numList = []
    # x = random.randint(1,10)
    # numList.append(x)
    # print(numList)

    while(userResponse.upper()!="NO"):
        userResponse=input("Would you like to continue adding elements to the list? YES/NO: ")
        if(userResponse.upper()=="NO"):
            break
        elif(userResponse.upper() == "YES"):
            x = random.randint(1,10)
            numList.append(x)
            print(numList)
        else:
            print("Enter valid response")
    return numList


    # print(x)


#2nd function: implementation of missing component (for which u created flowchart) and will accept list of integers returned from
#the 1st function as an argument and will return the modified list of integers (list after having some elements removed)
def modifyList(inputList):

    userResponse=""

    # if(len(inputList)>6):
    #     inputList.pop(6)

    while(userResponse.upper()!="NO"):
        userResponse= input("Would you like to continue removing value at index 6? YES/NO: ")
        if(len(inputList)>6):
            inputList.pop(6)
            print(inputList)
        else:
            # print(inputList)
            break

    return inputList    
    


#3rd function: implement everything after the missing component up to (but not including) printing the final result to the terminal
#3rd function: will accept the list of integers returned by the 2nd function as an argument and will process the elements of ur
#initial list into a new list, then it will return that new list to be printed out in your main() function
#THIS IS A PLACEHOLDER FUNCTION, meaning it must accept the argument list of integers and return that same list of integers 
#*UNMODIFIED*
#NON-RECURSIVE
def createNewList(initialList):
    newList=[]
    
    i=0
    while(i<len(initialList)):
        if(initialList[i]>3):
            # print(initialList)
            newList.append(initialList[i])
            # print(newList)
   
        i+=1
    
    # print(newList)
    return newList

# def createNewListRecursive(initialList):
    #Q.1 What was the base case of the argument for the recursive implementation of the third function?
    #ANS:
    #Q.2 How did you simplify an argument that was not the base case so that it is closer to the base case?
    #ANS:
    #Q.3 What additional operations did you perform on the return value from your recursive call in order to complete the operation?
    #ANS:

    #we have to call createNewListRecursive with a new input every time
    
    # lst=[1,2,3,4,5,6,7,8,9,10]
        
    # def valueGreaterThan3(lst, index=0):
    #     if index == len(lst):
    #         return []
        
    #     if (lst[index]>3):
    #         return [lst[index]] + valueGreaterThan3(lst, index + 1)
    #     else:
    #         return valueGreaterThan3(lst, index + 1)

    # print(valueGreaterThan3(lst))

def getAbove3(currList,index=0):
    if(index==len(currList)):
        return currList
    else:
        if(currList[index]<=3):
            # print(f"BEFORE {currList} ")
            # print(f"B.INDEX: {index}")
            del currList[index]
            # print(f"AFTER: {currList}")
            #index+=1;
            # print(f"A.INDEX: {index}")
            return getAbove3(currList,index)
            
        else:
            index+=1
            return getAbove3(currList,index)
   



def main():
    currList=createList()
    print(f"THE LIST: {currList}")
    currList1=modifyList(currList)
    print(f"THE MODIFIED LIST: {currList1}")
    currList2=createNewList(currList1)
    print(f"THE FINAL MODIFIED LIST: {currList2}")
    currList3=getAbove3(currList1)
    print(f"THE FINAL MODIFIED LIST WITH RECURSIVE FUNCTION: {currList3}")



main()
