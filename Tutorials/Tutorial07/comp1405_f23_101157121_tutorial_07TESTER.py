#Name: Maansinh Jadeja
#Student Number: 101157121

import random

def printMenu()->str: #Type-hinted function to print the menu

    userInput=""


    while(userInput!="a" and userInput!="b" and userInput!="c" and userInput!="d"): #Post-condition loop for modifying the list
        # userInput=printMenu()
        print()
        print("Please select one of the following options:")
        print(" a. Insert a random value at the front of the list")
        print(" b. Append a random value to the back of the list")
        print(" c. Pop (i.e., remove) the last value added")
        print(" d. Quit (and print the length)")
        userInput=input(">>")
            


    
    return userInput


def main():

    

    listOfValues=[] #Array that will hold the values 

    lengthOfList=0 #Variable that will update with each insert and remove for the length of the list

    # userInput=printMenu()


    while(True): #Post-condition loop for modifying the list
        userInput=printMenu()
        if(userInput=="d"):
            break

        elif(userInput=="a"):

            randomValue = random.randint(0,10)
            listOfValues.insert(0,randomValue)
            lengthOfList+=1
            print("The list is currently ",listOfValues)
                
        elif(userInput=="b"):

            randomValue = random.randint(0,10)
            listOfValues.append(randomValue)
            lengthOfList+=1
            print("The list is currently ",listOfValues)

        elif(userInput=="c"):

            lastValue = listOfValues.pop()
            lengthOfList-=1

            print("The list is currently ",listOfValues)
            
        else: 
            break
            # print("ERROR: INVALID INPUT!")
      
        

    #post condition loop
        

    print("Length of the list: ",lengthOfList)
        
                
   

main()


