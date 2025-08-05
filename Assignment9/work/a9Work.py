#Name: Maansinh Jadeja
#Student Number: 101157121

import sys
import random

def shiftingElements(theList, firstIndex, secondIndex):

    print()
    print("WE ARE IN SHIFTING ELEMENTS NOW!")

    print("The List: ",theList)
    print("First Index: ",firstIndex)
    print("Second Index: ",secondIndex)

    valueToShift = theList[firstIndex]

    for i in range(0,secondIndex+1):
        theList[i]=theList[i+1]
    
    theList[secondIndex]=valueToShift
    
    print("FINAL LIST: ",theList)

    

def newColourAnomaly():

    currColours = ["Black","Red","Blue"] #these colours are already present in the RunGame.py program

    newColours = ["Yellow","Green","White"] 

    currRoom = ["Gas Stove", "Retro Red Metal Refrigerator", "Oak Wooden Table", "4 Wooden Chairs"]

    # stringFormOfCurrRoom = str(currRoom)
    # print(f"Type of string form: {type(stringFormOfCurrRoom)} and value: {stringFormOfCurrRoom}")

    # stringFormOfCurrRoom = stringFormOfCurrRoom.replace("Black","White")
    # print(f"New String Form of currRoom: {stringFormOfCurrRoom}")

    # finalListFormOfCurrRoom = stringFormOfCurrRoom[1:len(stringFormOfCurrRoom)-1].split(",")
    # print(f"Type of new List: type{finalListFormOfCurrRoom} and first item: {finalListFormOfCurrRoom[0]}")

    print(f"CURR THINGS IN CURRROOM: {currRoom}")

    newListOfCurrRoom=[]

    indexOfColouredObject=0

    for colour in currColours:
        for things in currRoom:
            print(f"Things: {things}")
            if(colour in things):
                print("here")
                indexOfColouredObject=currRoom.index(things)
                randomValue = random.randint(0,2)
                newThings = things.replace(colour,newColours[randomValue])
                print(f"NEW THING: {newThings}")
                newListOfCurrRoom.append(newThings)
                currRoom.remove(things)
                print(currRoom)
    
    print("INDEX OF COLOURED OBJECT: ",indexOfColouredObject)

    #NOW TO MAINTAIN ORDER WE HAVE TO SWITCH VALUE AT INDEX 0 WITH VALUE AT indexOfColouredObject
    for items in currRoom:
        if((items in newListOfCurrRoom)==False):
            newListOfCurrRoom.append(items)

    firstThing = newListOfCurrRoom[0]
    secondThing = newListOfCurrRoom[indexOfColouredObject]

    print("firstThing: ",firstThing)
    print("secondThing: ",secondThing)

    shiftingElements(newListOfCurrRoom,0,indexOfColouredObject)



    print()
    print(f"NEW THINGS IN CURR ROOM IN ORDER: {newListOfCurrRoom}")


def main():

    numberOfCommandLineArguments = len(sys.argv)

    print(f"Array of arguements ({numberOfCommandLineArguments}): ", str(sys.argv))

    if(len(sys.argv)<2):
        print("ERROR: INPUT FILE NOT SPECIFIED")
    else:
        textFileName = sys.argv[1]
        print(f"Text File Name: {textFileName}")

        textFile = open(textFileName, "r")

        while (True):
            fileData = textFile.readline()

            if(fileData==""):
                break
            else:
                fileData=fileData.split("-")
                print(fileData)
                newRoom = fileData[0]
                newRoomFurniture = fileData[1].split(",")
                print(f"NEW ROOM: {newRoom}")
                print(f"NEW ROOM FURNITURE: {newRoomFurniture}")

# main()
print()
print("TESTING NEW COLOUR ANOMALY:")
newColourAnomaly()


