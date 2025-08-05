#Name: Maansinh Jadeja
#Student Number: 101157121

import random

def main():

    listOfValues=[]

    n=input("How long would you like the initial list to be? ")

    if(n.isnumeric()==False):
        print("ERROR: INVALID INPUT!")
    else:
        n = int(float(n))
        if(n<0):
            print("ERROR: INVALID INPUT!")
        else:
            for i in range(0,n):
                #input list with n random integers
                value = random.randint(0,10)
                listOfValues.append(value)
            
            print("The list is currently: "+str(listOfValues))

            userResponse=input("What number would you like to replace (or -1 to exit)? ")
            while(userResponse!="-1" and userResponse.isnumeric()):
                replacementString=input("What string would you like to use as a replacement? ")
                for values in listOfValues:
                    if(values==int(float(userResponse))):
                        index=listOfValues.index(values)
                        listOfValues[index]=replacementString

                # indexOfReplacingValue = listOfValues.index(int(float(userResponse)))#we have to replace all values not just 1
                # listOfValues[indexOfReplacingValue]=replacementString
                print("The list is currently: "+str(listOfValues))
                userResponse=input("What number would you like to replace (or -1 to exit)? ")
            

main()