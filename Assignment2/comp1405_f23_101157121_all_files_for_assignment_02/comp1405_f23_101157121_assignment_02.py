#Name: Maansinh Jadeja
#Student Number: 101157121
#Assignment 2
# import random 
import sys

def pipeline1():

    #Select a random positive integer less than 20
    # randomValue = random.randint(0,20)
    # print(sys.argv)
    # print(sys.argv[0])

    if(len(sys.argv)!=2 or (sys.argv[1].isnumeric()==False)):
        print("ERROR: PLEASE ENTER A REAL NUMBER AS A COMMAND LINE ARGUMENT")
        exit()

    randomValue = (input("Please enter a random positive integer less than 20: "))
    if(randomValue.isnumeric() and int(randomValue)<20):
    
        randomValue = int(randomValue)
        #floor divide the number to the left by 8
        randomValue = randomValue//8

        #Check your assigned pipeline and write the formatted output here
        print("Pipeline 1, current value: ",randomValue)

        #Add together the number to the left and 7
        randomValue = randomValue+7

        #Multiply the number to the left and 9
        randomValue = randomValue*9

        #Check your assigned pipleline for if this should be real or a character and either write a random real (noninteger) value 
        #or a random letter and the integer to which it will be converted 
        commandLineArgNum = int(sys.argv[1])
        # randomLetter='w'
        # numberOfRandomLetter=ord(randomLetter)

        #Multiply the number to the left and the number received above
        randomValue = randomValue*commandLineArgNum

        #Write the final value that will be in your assigned pipeline
        print("Final value in First Pipleine: ",randomValue)  
    
    else:
        print("ERROR: PLEASE ENTER A NUMBER LESS THAN 20 AT THE INPUT")
        exit()


def main():
    pipeline1()
    

main()