#Name: Maansinh Jadeja
#Student Number: 101157121 
#Assignment 11
import random
import sys

def createRoomAdjacencyList(roomList):
    
    roomDescriptionAdjacencyList=[]
    for i in range(0, len(roomList)):
        roomAndDescription = roomList[i].split(":")
        # print(f"TITLE: {roomAndDescription[0]}")
        # print(f"DESCRIPTION: {roomAndDescription[1]}")
        description = []
        description.append(roomAndDescription[0])
        description.append(roomAndDescription[1])
        roomDescriptionAdjacencyList.append(description)
        # roomDescrptionAdjacencyList.append(roomAndDescription[0])
        # roomDescrptionAdjacencyList.append(description)
    
    # print("TESTER")
    # # print(roomDescrptionAdjacencyList)
    # print(roomDescriptionAdjacencyList[0][0]) #Name Of Room
    # print(roomDescriptionAdjacencyList[0][1]) #Description of Room
    # # print(roomDescrptionAdjacencyList)
    # #[room[objects],room2[objects2]] -> list[0]

    return roomDescriptionAdjacencyList



def createRoomObjectAdjacencyList(objectList):

    # print()
    # print("create room object adjacency list")
    # print()

    roomObjectDescriptionAdjacencyList=[]

    # print()
    
    for i in range(0,len(objectList)-1):
        listOfRoomNameAndDescription = objectList[i].split(">")
        # print(listOfRoomNameAndDescription[0])#name of room
        # print(listOfRoomNameAndDescription[1])
        listOfObjects = listOfRoomNameAndDescription[1].split("+")
        description=[]
        description.append(listOfRoomNameAndDescription[0])
        description.append(listOfObjects)
        roomObjectDescriptionAdjacencyList.append(description)
        # break

    # print("TESTING OBJECTS LIST:")
    # # print(roomObjectDescriptionAdjacencyList)
    # print(roomObjectDescriptionAdjacencyList[0][0]) #Name of Room
    # print(roomObjectDescriptionAdjacencyList[0][1]) #List of Objects in the room

    return roomObjectDescriptionAdjacencyList
    

def createRoomListWithDirectionsAdjacencyList(directionList):

    # print()
    # print("create room with direction adjacency list")
    # print()
    # print(f"THE DIRECTION LIST IN ADJACENCY FUNCTION {directionList}")

    roomWithDirectionAdjacencyList=[]

    for i in range(0,len(directionList)):
        listOfRoomNameAndDirections = directionList[i].split(">")
        # print(listOfRoomNameAndDirections[0])
        # print(listOfRoomNameAndDirections[1])
        description=[]
        listOfDirections = listOfRoomNameAndDirections[1].split("+")
        description.append(listOfRoomNameAndDirections[0])
        description.append(listOfDirections)
        roomWithDirectionAdjacencyList.append(description)

        # break

    # print(f"THE FINAL DIRECTION LIST {roomWithDirectionAdjacencyList}")
    # print()
    # print("TESTING DIRECTION LIST:")
    # print(roomWithDirectionAdjacencyList)
    # print(roomWithDirectionAdjacencyList[0][0])#ROOM NAME
    # print(roomWithDirectionAdjacencyList[0][1])#LIST OF DIRECTIONS

    return roomWithDirectionAdjacencyList

def presentRoom(theRoomList,theNameOfRoom):
    # print(theRoomList)
    print()
    print("CURRENT ROOM:")

    # print(f"{theRoomList[givenIndex][0]}:{theRoomList[givenIndex][1]}")
    theIndex=-1
    for i in range(0,len(theRoomList)-1):
        if(theRoomList[i][0]==theNameOfRoom):
            print(f"{theRoomList[i][0]}:{theRoomList[i][1]}")
            theIndex=i

    
    return theRoomList[theIndex][0]

def displayObjects(theRoomObjectList, theNameOfRoom):
    print()
    # print("OBJECT LIST:")
    # print(f"INSIDE THE DISPLAYOBJECT FUNCTION: {theRoomObjectList}")
    # print(theNameOfRoom)
    # print(theRoomObjectList)
    # print(len(theRoomObjectList[0]))#THIS HOLDS NAME AND LIST OF OBJECTS
    # print(theRoomObjectList[0][0])
    # print(len(theRoomObjectList[0][1]))
    # print(f"THE LEN OF THE ROOM OBJECT LIST {len(theRoomObjectList)}")
    for i in range(0, len(theRoomObjectList)):
        # print(f"THE INDEX: {i}")
        if(theRoomObjectList[i][0]==theNameOfRoom):
            # print(f"Name of the room: {theRoomObjectList[i][0]}")
            # print(len(theRoomObjectList[i][1]))
            for j in range(0, len(theRoomObjectList[i][1])):
                print(theRoomObjectList[i][1][j])
                  
    
    print()
    # print(roomObjectDescriptionAdjacencyList[0][0]) #Name of Room
    # print(roomObjectDescriptionAdjacencyList[0][1]) #List of Objects in the room
    # for i in range(0, len(theRoomObjectList[givenIndex][1])):
    #     print(theRoomObjectList[givenIndex][1][i])


def displayDirections(theRoomList, theRoomObjects, theRoomDirectionList, theNameOfRoom):
    print()
    # print("ROOM DIRECTION:")
    # print(theNameOfRoom)

    # print(theRoomDirectionList[0])#THIS HOLDS ROOM NAME AND LIST OF DIRECTIONS
    # print(theRoomDirectionList[0][0]) #name of the room
    # print(theRoomDirectionList[0][1]) #list of directions in the room



    for i in range(0, len(theRoomDirectionList)):
        if(theRoomDirectionList[i][0]==theNameOfRoom):
            # print(f"Name of the room: {theRoomDirectionList[i][0]}")
            for j in range(0, len(theRoomDirectionList[i][1])):
                print(f"[{j}] {theRoomDirectionList[i][1][j]}")
            
            userInput=""
            while(userInput!="-1"):
                userInput = input("SELECT DIRECTION (-1 TO EXIT): ")
                if(userInput=="-1"):
                    break
                if(userInput.isnumeric()==False):
                    print("ERROR: INVALID INPUT!")
                else:
                    if((0<=int(userInput) and int(userInput)<len(theRoomDirectionList[i][1]))==False):
                        print("ERROR: CHOOSE ONE OF THE NUMBER")
                    else:
                        directionSelected = theRoomDirectionList[i][1][int(userInput)]
                        print(f"Direction Selected: {directionSelected}")
                        indexOfOpeningBracket = directionSelected.index("[")
                        indexOfClosingBracket = directionSelected.index("]")
                        roomDetails = directionSelected[indexOfOpeningBracket+1:indexOfClosingBracket]
                        indexOfSpaceSeperator = roomDetails.index(" ")
                        newRoomName = roomDetails[indexOfSpaceSeperator+1:len(roomDetails)]
                        # print(newRoomName)
                        promptUser(theRoomList, theRoomObjects, theRoomDirectionList, newRoomName)
                
                

    
    
    # print(roomWithDirectionAdjacencyList[0][0])#ROOM NAME
    # print(roomWithDirectionAdjacencyList[0][1])#LIST OF DIRECTIONS


def promptUser(roomList, roomObjects, roomDirections, nameOfRoom):
    
    presentRoom(roomList,nameOfRoom)
    # print()
    # print(f"THE ROOM LIST IN promptUser FUNCTION {roomList}")
    # print()
    # print(f"THE OBJECT LIST IN promptUser FUNCTION {roomObjects}")
    # print()
    # print(f"THE DIRECTION LIST IN promptUser FUNCTION {roomDirections}")
    # print()


    userInput=""

    while(userInput!="-1"):
        print("[1] DISPLAY OBJECTS")
        print("[2] DISPLAY DIRECTIONS")
        userInput = input("SELECT COMMAND (-1 TO EXIT): ")
        if(userInput=="-1"):
            print("THANK YOU FOR PLAYING")
            # break
            exit() #CAN WE USE THE EXIT() FUNCTION?
        if(userInput=="1"):
            displayObjects(roomObjects,nameOfRoom)
        if(userInput=="2"):
            displayDirections(roomList, roomObjects,roomDirections, nameOfRoom)
            # break
    
    # print("THANK YOU FOR PLAYING")


def runGame(roomList, roomObjects, roomDirections):
    # # print(f"THE ROOM LIST IN RUNGAME FUNCTION {roomList}")
    # print()
    # print(f"THE OBJECT LIST IN RUNGAME FUNCTION {roomObjects}")
    # print()

    # print(f"THE DIRECTION LIST IN RUNGAME FUNCTION {roomDirections}")


    print("GAME BEGIN")
    roomIndex = random.randint(0,len(roomList)-1)
    # nameOfRoom = presentRoom(roomList,roomIndex)
    nameOfRoom = roomList[roomIndex][0]
    # print(f"NAME OF ROOM IN RUNGAME: {nameOfRoom}")
    # presentRoom(roomList,nameOfRoom)
    promptUser(roomList, roomObjects, roomDirections, nameOfRoom)

    


def main():
    
    dataFile = open("comp1405_f23_101157121_assignment_10_data.txt", "r")
    # print(dataFile.readLine())
    fileData = dataFile.read()

    # print(fileData[0])
    # print(fileData[1])
    # print(len(fileData))
    
    fileDataLinesArray = fileData.split("\n")
    # print(fileDataLinesArray[0])
    # print(fileDataLinesArray[1])

    
    roomListWithDescription=[]
    objectsInEachRoomWithDescription=[]
    roomListWithDirections=[]
    startingIndexOfObjectList=-1
    endingIndexOfObjectList=-1
    startingIndexOfDirectionList=-1

    for i in range(0,len(fileDataLinesArray)):
        if(fileDataLinesArray[i]=="#The Rooms"):
            roomListWithTitle=fileDataLinesArray[i+1].split(">")
            roomListWithDescription = roomListWithTitle[1].split("+")
        if(fileDataLinesArray[i]=="#The objects in each room"):
            startingIndexOfObjectList=i+1
        if(fileDataLinesArray[i]=="#Room Directions"):
            endingIndexOfObjectList=i
            startingIndexOfDirectionList=i+1


    # print("START")
    # print(roomListWithDescription[0])
    # print("END")
    # print(f"THE ROOM LIST WITH DESCRIPTION: {roomListWithDescription}")
    # createRoomAdjacencyList(roomListWithDescription)

    for indices in range(startingIndexOfObjectList, endingIndexOfObjectList+1):

        objectsInEachRoomWithDescription.append(fileDataLinesArray[indices])


    # createRoomObjectAdjacencyList(objectsInEachRoomWithDescription)

    for x in range(startingIndexOfDirectionList, len(fileDataLinesArray)):
        roomListWithDirections.append(fileDataLinesArray[x])
    
    # print(f"THE ROOM LIST WITH DIRECTIONS: {roomListWithDirections}")
    # print()
    # print()
    # print()
    # print(roomListWithDirections)
    # createRoomListWithDirectionsAdjacencyList(roomListWithDirections)

    runGame(createRoomAdjacencyList(roomListWithDescription), createRoomObjectAdjacencyList(objectsInEachRoomWithDescription), createRoomListWithDirectionsAdjacencyList(roomListWithDirections))


 

main()
